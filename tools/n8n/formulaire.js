import { workflow, node, trigger, ifElse, expr } from '@n8n/workflow-sdk';

const GMAIL = { gmailOAuth2: { id: 'vRCFD0KqJLrdMvnt', name: 'Gmail account' } };

const reception = trigger({
  type: 'n8n-nodes-base.webhook',
  version: 2.1,
  config: {
    name: 'Réception du formulaire',
    parameters: { httpMethod: 'POST', path: 'architecte-commerce-demande-5d8e2a71c4f9b036', authentication: 'none', responseMode: 'responseNode' }
  }
});

const valider = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Valider et préparer',
    parameters: {
      language: 'javaScript',
      mode: 'runOnceForAllItems',
      jsCode: `const b = $input.first().json.body || {};
const one = (v, max) => String(v === undefined || v === null ? '' : v).replace(/[\\u0000-\\u001F]+/g, ' ').replace(/ +/g, ' ').trim().slice(0, max);
const multi = (v, max) => String(v === undefined || v === null ? '' : v).replace(/[\\u0000-\\u0008\\u000B\\u000C\\u000E-\\u001F]/g, '').replace(/\\r\\n?/g, '\\n').trim().slice(0, max);
const d = {
  nom: one(b.nom, 120), societe: one(b.societe, 140), email: one(b.email, 160), tel: one(b.tel, 40),
  activite: one(b.activite, 80), adresse: one(b.adresse, 160), surface: one(b.surface, 20), etape: one(b.etape, 100),
  echeance: one(b.echeance, 60), source: one(b.source, 80), message: multi(b.message, 4000)
};
const piege = one(b.site_web, 100);
const emailOk = /^[^ @,;<>]+@[^ @,;<>]+[.][^ @,;<>]{2,}$/.test(d.email);
const requis = !!(d.nom && emailOk && d.activite && d.adresse && d.etape && d.message);
const sd = $getWorkflowStaticData('global');
const now = Date.now();
sd.horodatages = (sd.horodatages || []).filter((t) => now - t < 3600000);
let statut = 'ok';
if (piege) statut = 'piege';
else if (!requis) statut = 'invalide';
else if (sd.horodatages.length >= 20) statut = 'limite';
if (statut === 'ok') sd.horodatages.push(now);
const quand = new Date().toLocaleString('fr-FR', { timeZone: 'Europe/Paris' });
const v = (x) => (x ? x : 'non précisé');
const lignes = [
  'Nouvelle demande reçue par le formulaire de architecte-commerce.fr (FIXIA)',
  'Reçue le : ' + quand,
  'Page d\u2019origine : ' + v(d.source),
  '',
  'CONTACT',
  'Nom : ' + d.nom,
  'Société ou enseigne : ' + v(d.societe),
  'Courriel : ' + d.email,
  'Téléphone : ' + v(d.tel),
  '',
  'PROJET',
  'Activité : ' + d.activite,
  'Adresse ou quartier du local : ' + d.adresse,
  'Surface (m²) : ' + v(d.surface),
  'Avancement : ' + d.etape,
  'Ouverture souhaitée : ' + v(d.echeance),
  '',
  'MESSAGE',
  d.message
];
const sujet = ('Architecte commerce \u2014 ' + d.activite + ' \u2014 ' + d.adresse + ' \u2014 ' + d.nom).slice(0, 150);
return [{ json: { statut, accuse: statut === 'ok', email: d.email, sujet, corps: lignes.join('\\n') } }];`
    }
  }
});

const valide = ifElse({
  version: 2.2,
  config: {
    name: 'Demande valide ?',
    parameters: {
      conditions: {
        options: { caseSensitive: true, leftValue: '', typeValidation: 'strict' },
        conditions: [{ leftValue: expr('{{ $json.statut }}'), operator: { type: 'string', operation: 'equals' }, rightValue: 'ok' }],
        combinator: 'and'
      }
    }
  }
});

const prevenir = node({
  type: 'n8n-nodes-base.gmail',
  version: 2.2,
  config: {
    name: 'Prévenir l’architecte',
    onError: 'continueRegularOutput',
    credentials: GMAIL,
    parameters: {
      resource: 'message', operation: 'send', authentication: 'oAuth2',
      sendTo: 'analyse@fixia.fr',
      subject: expr('{{ $("Valider et préparer").first().json.sujet }}'),
      emailType: 'text',
      message: expr('{{ $("Valider et préparer").first().json.corps }}'),
      options: { appendAttribution: false, senderName: 'FIXIA architecte-commerce.fr (formulaire)', replyTo: expr('{{ $("Valider et préparer").first().json.email }}') }
    }
  }
});

const envoye = ifElse({
  version: 2.2,
  config: {
    name: 'Courriel envoyé ?',
    parameters: {
      conditions: {
        options: { caseSensitive: true, leftValue: '', typeValidation: 'strict' },
        conditions: [{ leftValue: expr('{{ $json.id }}'), operator: { type: 'string', operation: 'notEmpty' }, rightValue: '' }],
        combinator: 'and'
      }
    }
  }
});

const accuse = node({
  type: 'n8n-nodes-base.gmail',
  version: 2.2,
  config: {
    name: 'Accusé de réception',
    onError: 'continueRegularOutput',
    credentials: GMAIL,
    parameters: {
      resource: 'message', operation: 'send', authentication: 'oAuth2',
      sendTo: expr('{{ $("Valider et préparer").first().json.email }}'),
      subject: 'Votre demande a bien été reçue — FIXIA Architecte',
      emailType: 'text',
      message: 'Bonjour,\n\nVotre demande est bien arrivée. Nous l’étudions et revenons vers vous par courriel ou par téléphone.\n\nSi votre demande est urgente, vous pouvez nous joindre au 09 70 70 17 99.\n\nCet accusé de réception est automatique. Il ne constitue ni un devis, ni un engagement, ni un avis sur votre projet.\n\nLes informations transmises servent uniquement à répondre à votre demande. Vos droits et la durée de conservation : https://architecte-commerce.fr/confidentialite\n\nFIXIA Architecte, architecte de commerces à Paris\nQuentin Piepszownik, architecte, entrepreneur individuel\n71 rue du Cherche-Midi, 75006 Paris\nhttps://architecte-commerce.fr',
      options: { appendAttribution: false, senderName: 'FIXIA Architecte' }
    }
  }
});

const merci = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: { name: 'Merci', parameters: { respondWith: 'redirect', redirectURL: 'https://architecte-commerce.fr/etudier-mon-projet/merci', options: { responseCode: 303 } } }
});

const erreurEnvoi = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: { name: 'Erreur d’envoi', parameters: { respondWith: 'redirect', redirectURL: 'https://architecte-commerce.fr/etudier-mon-projet#erreur', options: { responseCode: 303 } } }
});

const erreurSaisie = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: { name: 'Erreur de saisie', parameters: { respondWith: 'redirect', redirectURL: 'https://architecte-commerce.fr/etudier-mon-projet#erreur', options: { responseCode: 303 } } }
});

const merciIgnore = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: { name: 'Merci (demande ignorée)', parameters: { respondWith: 'redirect', redirectURL: 'https://architecte-commerce.fr/etudier-mon-projet/merci', options: { responseCode: 303 } } }
});

const incomplete = ifElse({
  version: 2.2,
  config: {
    name: 'Demande incomplète ?',
    parameters: {
      conditions: {
        options: { caseSensitive: true, leftValue: '', typeValidation: 'strict' },
        conditions: [{ leftValue: expr('{{ $json.statut }}'), operator: { type: 'string', operation: 'equals' }, rightValue: 'invalide' }],
        combinator: 'and'
      }
    }
  }
});

export default workflow('architecte-commerce-formulaire', 'ARCHITECTE COMMERCE (FIXIA) — formulaire de contact (production)')
  .add(reception)
  .to(valider)
  .to(valide
    .onTrue(prevenir.to(envoye
      .onTrue(accuse.to(merci))
      .onFalse(erreurEnvoi)))
    .onFalse(incomplete
      .onTrue(erreurSaisie)
      .onFalse(merciIgnore)));
