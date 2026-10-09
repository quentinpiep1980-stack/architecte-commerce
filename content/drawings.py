# -*- coding: utf-8 -*-
"""Dessins vectoriels du site (style « tirage de plan »), générés en SVG.

- elevation() : élévation sur rue d'un rez-de-chaussée parisien ; la devanture centrale change avec l'activité
  (boutique, restaurant, institut, boulangerie, showroom). Les annotations ne portent que des règles sourcées.
- devanture(act) : la devanture seule, pour les vignettes d'activité.
- plan_local() : plan d'un local commercial avec les points à vérifier avant de signer.
Les dessins sont des illustrations : aucune cote de projet réel n'y figure.
"""

M = 46  # unités par mètre (élévation)
X0 = 63  # origine des travées
BAY = 161  # travée de 3,50 m
PIER = 25
GROUND = 540
RDC_TOP = 338
ENT_TOP = 218
F1_TOP = 75

ACTS = [
    ("boutique", "Boutique", "BOUTIQUE"),
    ("restaurant", "Restaurant", "RESTAURANT"),
    ("beaute", "Institut", "INSTITUT"),
    ("bouche", "Boulangerie", "BOULANGERIE"),
    ("showroom", "Showroom", "SHOWROOM"),
]


def f(v):
    return ('%.1f' % v).rstrip('0').rstrip('.')


def line(x1, y1, x2, y2, cls='ln'):
    return f'<line class="{cls}" x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}"/>'


def rect(x, y, w, h, cls='ln', rx=0):
    r = f' rx="{f(rx)}"' if rx else ''
    return f'<rect class="{cls}" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}"{r}/>'


def path(d, cls='ln'):
    return f'<path class="{cls}" d="{d}"/>'


def circle(cx, cy, r, cls='ln'):
    return f'<circle class="{cls}" cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}"/>'


def bx(i):
    return X0 + i * BAY


# ---------------------------------------------------------------- intérieurs (dessinés dans la vitrine)
def interior(act, L, R, top, bot):
    """Mobilier vu à travers le vitrage. L/R : bords gauche et droit de la zone vitrée, porte au centre."""
    c = (L + R) / 2
    lv = (L + 6, c - 40)  # vitrine gauche
    rv = (c + 40, R - 6)  # vitrine droite
    out = []
    a = out.append
    floor = bot
    if act == 'boutique':
        # portant avec cintres et vêtements
        x1, x2 = lv[0] + 10, lv[1] - 10
        ry = top + 22
        a(line(x1, ry, x2, ry, 'int'))
        a(line(x1 + 4, ry, x1 + 4, floor, 'int')); a(line(x2 - 4, ry, x2 - 4, floor, 'int'))
        n = 7
        for k in range(n):
            x = x1 + 16 + k * (x2 - x1 - 32) / (n - 1)
            h = 46 + (k % 3) * 9
            a(path(f'M{f(x)} {f(ry)} l-8 8 h16 z', 'int'))
            a(path(f'M{f(x-9)} {f(ry+8)} L{f(x-12)} {f(ry+8+h)} L{f(x+12)} {f(ry+8+h)} L{f(x+9)} {f(ry+8)}', 'int'))
        # table de présentation et piles pliées, buste
        tx1, tx2, ty = rv[0] + 14, rv[0] + 110, floor - 34
        a(line(tx1, ty, tx2, ty, 'int')); a(line(tx1 + 6, ty, tx1 + 6, floor, 'int')); a(line(tx2 - 6, ty, tx2 - 6, floor, 'int'))
        for k, w in enumerate((26, 22, 28)):
            x = tx1 + 10 + k * 32
            for j in range(3):
                a(rect(x, ty - 6 * (j + 1), w, 5, 'int'))
        bxx = rv[1] - 34
        a(circle(bxx, top + 30, 8, 'int'))
        a(path(f'M{f(bxx-6)} {f(top+40)} Q{f(bxx-20)} {f(top+70)} {f(bxx-12)} {f(top+96)} L{f(bxx+12)} {f(top+96)} Q{f(bxx+20)} {f(top+70)} {f(bxx+6)} {f(top+40)} Z', 'int'))
        a(line(bxx, top + 96, bxx, floor, 'int')); a(line(bxx - 12, floor, bxx + 12, floor, 'int'))
    elif act == 'restaurant':
        # suspensions
        for x in (lv[0] + 45, lv[1] - 45, rv[0] + 50):
            a(line(x, top, x, top + 20, 'int'))
            a(path(f'M{f(x-12)} {f(top+30)} Q{f(x)} {f(top+12)} {f(x+12)} {f(top+30)} Z', 'int'))
        # tables bistrot et chaises
        for x in (lv[0] + 45, lv[1] - 45):
            ty = floor - 40
            a(line(x - 20, ty, x + 20, ty, 'int')); a(line(x, ty, x, floor, 'int')); a(line(x - 10, floor, x + 10, floor, 'int'))
            for s in (-1, 1):
                cx = x + s * 32
                a(path(f'M{f(cx - s*2)} {f(floor - 62)} Q{f(cx + s*6)} {f(floor - 50)} {f(cx + s*4)} {f(floor - 26)} L{f(cx - s*10)} {f(floor - 26)} M{f(cx + s*4)} {f(floor - 26)} L{f(cx + s*6)} {f(floor)} M{f(cx - s*10)} {f(floor - 26)} L{f(cx - s*12)} {f(floor)}', 'int'))
        # comptoir, tabourets, étagères à bouteilles
        cx1, cx2 = rv[0] + 70, rv[1] - 4
        a(rect(cx1, floor - 44, cx2 - cx1, 44, 'int'))
        for k in range(3):
            y = top + 18 + k * 18
            a(line(cx1 + 6, y, cx2 - 6, y, 'int'))
            for j in range(6):
                bxp = cx1 + 14 + j * (cx2 - cx1 - 28) / 5
                a(path(f'M{f(bxp-3)} {f(y)} v-9 l2 -4 v-3 h2 v3 l2 4 v9', 'int'))
        for x in (rv[0] + 40,):
            a(line(x - 9, floor - 36, x + 9, floor - 36, 'int')); a(line(x - 6, floor - 36, x - 9, floor, 'int')); a(line(x + 6, floor - 36, x + 9, floor, 'int'))
    elif act == 'beaute':
        # miroirs ronds et fauteuils
        for x in (lv[0] + 48, lv[1] - 48):
            a(circle(x, top + 34, 22, 'int'))
            a(path(f'M{f(x-18)} {f(floor-60)} h36 v26 h-36 z M{f(x-22)} {f(floor-34)} h44 v8 h-44 z M{f(x)} {f(floor-26)} v20 M{f(x-14)} {f(floor)} h28', 'int'))
            a(line(x - 30, top + 66, x + 30, top + 66, 'int'))
        # banque d'accueil, étagère de produits, plante
        a(rect(rv[0] + 12, floor - 46, 90, 46, 'int'))
        a(line(rv[0] + 12, floor - 52, rv[0] + 102, floor - 52, 'int'))
        for k in range(2):
            y = top + 22 + k * 26
            a(line(rv[0] + 116, y, rv[1] - 8, y, 'int'))
            for j in range(5):
                bxp = rv[0] + 124 + j * 12
                a(rect(bxp, y - 14, 7, 14, 'int', 2))
        px = rv[1] - 24
        a(path(f'M{f(px-12)} {f(floor)} l3 -22 h18 l3 22 z M{f(px)} {f(floor-22)} C{f(px-30)} {f(floor-50)} {f(px-8)} {f(floor-70)} {f(px)} {f(floor-54)} C{f(px+8)} {f(floor-74)} {f(px+30)} {f(floor-48)} {f(px)} {f(floor-22)}', 'int'))
    elif act == 'bouche':
        # étagères à pain
        for k in range(3):
            y = top + 22 + k * 26
            a(line(lv[0] + 8, y, lv[1] - 8, y, 'int'))
            for j in range(6):
                ex = lv[0] + 22 + j * (lv[1] - lv[0] - 44) / 5
                if (j + k) % 2:
                    a(path(f'M{f(ex-12)} {f(y)} Q{f(ex)} {f(y-14)} {f(ex+12)} {f(y)} Z', 'int'))
                else:
                    a(rect(ex - 13, y - 9, 26, 9, 'int', 4))
        a(rect(lv[0] + 8, floor - 34, lv[1] - lv[0] - 16, 34, 'int'))
        # vitrine réfrigérée et présentoirs à gâteaux
        vx1, vx2 = rv[0] + 10, rv[1] - 10
        a(path(f'M{f(vx1)} {f(floor)} V{f(floor-40)} L{f(vx1+18)} {f(floor-64)} H{f(vx2)} V{f(floor)} Z', 'int'))
        a(line(vx1, floor - 40, vx2, floor - 40, 'int'))
        for j in range(4):
            gx = vx1 + 36 + j * (vx2 - vx1 - 60) / 3
            a(path(f'M{f(gx-12)} {f(floor-46)} h24 M{f(gx)} {f(floor-46)} v-3 M{f(gx-9)} {f(floor-49)} a9 6 0 0 1 18 0 z', 'int'))
    elif act == 'showroom':
        # canapé et lampadaire
        sx1, sx2 = lv[0] + 14, lv[1] - 40
        a(path(f'M{f(sx1)} {f(floor-8)} V{f(floor-48)} q0 -6 6 -6 H{f(sx2-6)} q6 0 6 6 V{f(floor-8)} Z M{f(sx1)} {f(floor-28)} H{f(sx2)} M{f(sx1+6)} {f(floor-8)} v8 M{f(sx2-6)} {f(floor-8)} v8', 'int'))
        lx = lv[1] - 18
        a(path(f'M{f(lx)} {f(floor)} V{f(top+40)} M{f(lx-14)} {f(top+40)} L{f(lx-6)} {f(top+18)} H{f(lx+6)} L{f(lx+14)} {f(top+40)} Z M{f(lx-10)} {f(floor)} h20', 'int'))
        # socles et objets, cadre
        for k, (w, h) in enumerate(((44, 52), (36, 34))):
            px = rv[0] + 16 + k * 70
            a(rect(px, floor - h, w, h, 'int'))
            if k == 0:
                a(path(f'M{f(px+14)} {f(floor-h)} q-6 -16 4 -30 h8 q10 14 4 30 z', 'int'))
            else:
                a(path(f'M{f(px+8)} {f(floor-h)} v-26 h20 v12 h-20 M{f(px+28)} {f(floor-h)} v-14', 'int'))
        a(rect(rv[1] - 64, top + 14, 54, 70, 'int'))
        a(path(f'M{f(rv[1]-58)} {f(top+70)} l14 -22 10 12 8 -10 16 20', 'int'))
    return ''.join(out)


# ---------------------------------------------------------------- devanture
def devanture_parts(act, L, R, sign, scale_note=True):
    """Devanture en applique entre L et R ; renvoie (fond éclairé, lignes, intérieur, enseigne)."""
    top = RDC_TOP - 8
    band_b = top + 36
    gl_t, gl_b = band_b + 8, GROUND - 34
    pil = 16
    c = (L + R) / 2
    door_w = 64
    g = []
    # cadre et bandeau d'enseigne
    body = rect(L, top, R - L, GROUND - top, 'fill-wood')
    g.append(rect(L, top, R - L, GROUND - top, 'ln ln-b'))
    g.append(line(L - 6, top, R + 6, top, 'ln ln-b'))
    g.append(line(L - 6, top - 5, R + 6, top - 5, 'ln'))
    g.append(rect(L + pil, top + 6, R - L - 2 * pil, 26, 'ln'))
    # pilastres
    for x in (L + pil, R - pil):
        g.append(line(x, band_b, x, GROUND, 'ln'))
    # soubassements (allèges) des vitrines
    g.append(rect(L + pil, gl_b, c - door_w / 2 - (L + pil), GROUND - gl_b, 'ln'))
    g.append(rect(c + door_w / 2, gl_b, R - pil - (c + door_w / 2), GROUND - gl_b, 'ln'))
    for x1, x2 in ((L + pil, c - door_w / 2), (c + door_w / 2, R - pil)):
        g.append(rect(x1 + 8, gl_b + 7, x2 - x1 - 16, GROUND - gl_b - 14, 'ln ln-t'))
    # vitrages et meneaux
    g.append(rect(L + pil, gl_t, c - door_w / 2 - (L + pil), gl_b - gl_t, 'ln'))
    g.append(rect(c + door_w / 2, gl_t, R - pil - (c + door_w / 2), gl_b - gl_t, 'ln'))
    g.append(line((L + pil + c - door_w / 2) / 2, gl_t, (L + pil + c - door_w / 2) / 2, gl_b, 'ln ln-t'))
    g.append(line((R - pil + c + door_w / 2) / 2, gl_t, (R - pil + c + door_w / 2) / 2, gl_b, 'ln ln-t'))
    # porte vitrée et imposte
    g.append(rect(c - door_w / 2, gl_t, door_w, GROUND - gl_t, 'ln'))
    g.append(line(c - door_w / 2, gl_t + 22, c + door_w / 2, gl_t + 22, 'ln'))
    g.append(rect(c - door_w / 2 + 6, gl_t + 28, door_w - 12, GROUND - gl_t - 34, 'ln ln-t'))
    g.append(line(c + door_w / 2 - 12, (gl_t + GROUND) / 2 - 8, c + door_w / 2 - 12, (gl_t + GROUND) / 2 + 8, 'ln ln-b'))
    lit = [rect(L + pil, gl_t, R - L - 2 * pil, gl_b - gl_t, 'lit'),
           rect(c - door_w / 2 + 6, gl_t + 28, door_w - 12, GROUND - gl_t - 34, 'lit')]
    inner = interior(act, L + pil, R - pil, gl_t + 4, gl_b)
    sign_svg = f'<text class="sign" x="{f(c)}" y="{f(top + 25)}" text-anchor="middle">{sign}</text>'
    return body + ''.join(lit), ''.join(g), inner, sign_svg, (gl_t, gl_b, door_w)


def awning(L, R):
    """Store banne vu en élévation (restaurant)."""
    y1, y2 = RDC_TOP + 34, RDC_TOP + 70
    out = [path(f'M{f(L-8)} {f(y1)} H{f(R+8)} L{f(R+14)} {f(y2)} H{f(L-14)} Z', 'ln ln-b fill-awn')]
    n = 22
    w = (R - L + 28) / n
    d = f'M{f(L-14)} {f(y2)}'
    for k in range(n):
        d += f' q{f(w/2)} 9 {f(w)} 0'
    out.append(path(d, 'ln'))
    for k in range(1, n, 2):
        x = L - 14 + k * w
        out.append(line(x - (k - n / 2) * 0.3, y1, x, y2, 'ln ln-t'))
    return ''.join(out)


def terrace(xs):
    out = []
    for x in xs:
        ty = GROUND + 2
        out.append(line(x - 16, ty - 28, x + 16, ty - 28, 'ln ln-b'))
        out.append(line(x, ty - 28, x, ty, 'ln'))
        for s in (-1, 1):
            cx = x + s * 26
            out.append(path(f'M{f(cx)} {f(ty-48)} Q{f(cx+s*6)} {f(ty-36)} {f(cx+s*4)} {f(ty-20)} L{f(cx-s*8)} {f(ty-20)} M{f(cx+s*4)} {f(ty-20)} L{f(cx+s*6)} {f(ty)} M{f(cx-s*8)} {f(ty-20)} L{f(cx-s*10)} {f(ty)}', 'ln'))
    return ''.join(out)


# ---------------------------------------------------------------- élévation complète
ANN = {
    # activité -> annotations (texte, ancre x, ancre y, position du texte x, y)
    'all': [
        ("Enseigne : autorisation du maire, 2 mois", "Code de l'environnement, R581-13", 'sign'),
        ("Dégagement de 0,90 m sous 20 personnes", "Règlement de sécurité, PE 11", 'door'),
        ("Devanture : retrait limité à 10–20 cm", "PLU de Paris, UG.2.1.4", 'plane'),
    ],
    'restaurant': [
        ("Air de cuisine rejeté à 8 m de toute fenêtre", "RSD de Paris, art. 63-1", 'duct'),
        ("Terrasse : autorisation de la Ville", "Règlement des étalages et terrasses", 'terrace'),
    ],
}


def ann_block(x, y, t1, t2, anchor='start'):
    w = max(len(t1), len(t2)) * 6.1 + 12
    bx0 = x - 6 if anchor == 'start' else x - w + 6
    return (f'<rect class="ann-bg" x="{f(bx0)}" y="{f(y-14)}" width="{f(w)}" height="36" rx="2"/>'f'<text class="ann" x="{f(x)}" y="{f(y)}" text-anchor="{anchor}">{t1}</text>'
            f'<text class="ann ann-src" x="{f(x)}" y="{f(y+15)}" text-anchor="{anchor}">{t2}</text>')


def elevation(active='boutique', uid='el'):
    W, H = 1600, 640
    L = bx(3)
    R = bx(6) + PIER
    c = (L + R) / 2
    o = []
    a = o.append
    a(f'<svg class="elev" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{uid}-t {uid}-d" data-act="{active}">')
    a(f'<title id="{uid}-t">Élévation sur rue d\'un rez-de-chaussée commercial parisien</title>')
    a(f'<desc id="{uid}-d">Dessin d\'illustration : un immeuble de pierre avec, au rez-de-chaussée, une devanture en applique dont l\'enseigne, le mobilier visible en vitrine et les règles annotées changent selon l\'activité choisie.</desc>')
    a('<defs>'
      f'<linearGradient id="{uid}-fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" style="stop-color:#133A63;stop-opacity:1"/><stop offset=".55" style="stop-color:#133A63;stop-opacity:.55"/><stop offset="1" style="stop-color:#133A63;stop-opacity:0"/></linearGradient>'
      f'<linearGradient id="{uid}-spill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="var(--vitrine)" stop-opacity=".55"/><stop offset="1" stop-color="var(--vitrine)" stop-opacity="0"/></linearGradient>'
      f'<clipPath id="{uid}-glass"><rect x="{f(L+16)}" y="{f(RDC_TOP+36)}" width="{f(R-L-32)}" height="{f(GROUND-34-RDC_TOP-36)}"/></clipPath>'
      '</defs>')
    a('<g class="facade">')
    # joints de pierre (assises) sur toute la hauteur, masqués ensuite par les baies
    y = GROUND - 22
    while y > F1_TOP - 60:
        a(line(0, y, W, y, 'ln ln-j'))
        y -= 22
    # bandeau entre entresol et étage, balcon filant léger
    a(rect(0, ENT_TOP - 10, W, 10, 'ln mask'))
    a(line(0, ENT_TOP - 14, W, ENT_TOP - 14, 'ln'))
    a(rect(0, RDC_TOP - 4, W, 4, 'ln mask'))
    # baies d'entresol et d'étage
    for i in range(-1, 10):
        x = bx(i) + PIER
        w = BAY - PIER
        cx = x + w / 2
        ew, eh = 62, 70
        a(rect(cx - ew / 2 - 6, ENT_TOP + 26 - 6, ew + 12, eh + 12, 'ln mask'))
        a(rect(cx - ew / 2, ENT_TOP + 26, ew, eh, 'ln mask-g'))
        a(line(cx, ENT_TOP + 26, cx, ENT_TOP + 26 + eh, 'ln ln-t'))
        fw, fh = 64, 118
        fy = F1_TOP + 12
        a(rect(cx - fw / 2 - 8, fy - 14, fw + 16, fh + 14, 'ln mask'))
        a(path(f'M{f(cx-fw/2-14)} {f(fy-14)} h{f(fw+28)} l-6 -10 h{f(-fw-16)} z', 'ln'))
        a(rect(cx - fw / 2, fy, fw, fh, 'ln mask-g'))
        a(line(cx, fy, cx, fy + fh, 'ln ln-t'))
        a(line(cx - fw / 2, fy + 40, cx + fw / 2, fy + 40, 'ln ln-t'))
        # balconnet
        by = fy + fh - 34
        a(rect(cx - fw / 2 - 10, by, fw + 20, 34, 'ln mask'))
        for k in range(9):
            xx = cx - fw / 2 - 6 + k * (fw + 12) / 8
            a(line(xx, by + 4, xx, by + 34, 'ln ln-t'))
        a(path(f'M{f(cx-14)} {f(by+19)} c4 -10 10 -10 14 0 c4 10 10 10 14 0 M{f(cx-14)} {f(by+19)} c4 10 10 10 14 0 c4 -10 10 -10 14 0', 'ln ln-t'))
        a(line(cx - fw / 2 - 12, by, cx + fw / 2 + 12, by, 'ln ln-b'))
    a('</g>')
    a(f'<rect x="0" y="0" width="{W}" height="{ENT_TOP+40}" fill="url(#{uid}-fade)"/>')
    # rez-de-chaussée : piles en pierre (refends)
    a('<g class="rdc">')
    for i in range(-1, 10):
        x = bx(i)
        a(rect(x, RDC_TOP, PIER, GROUND - RDC_TOP, 'ln mask'))
        yy = RDC_TOP + 20
        while yy < GROUND:
            a(line(x, yy, x + PIER, yy, 'ln ln-t'))
            yy += 20
    # voisin A (travées 0-1) : boutique fermée, devanture peinte
    for (i1, i2, kind) in ((-1, 1, 'shutter'), (2, 2, 'porte'), (6, 7, 'closed'), (8, 9, 'shutter')):
        xl, xr = bx(i1) + PIER, bx(i2 + 1)
        if kind == 'porte':
            cx = (xl + xr) / 2
            pw = xr - xl - 30
            a(path(f'M{f(cx-pw/2)} {f(GROUND)} V{f(RDC_TOP+70)} A{f(pw/2)} {f(pw/2)} 0 0 1 {f(cx+pw/2)} {f(RDC_TOP+70)} V{f(GROUND)} Z', 'ln ln-b mask'))
            a(line(cx, RDC_TOP + 70 - pw / 2, cx, GROUND, 'ln'))
            for k in range(3):
                yy = RDC_TOP + 90 + k * 46
                a(rect(cx - pw / 2 + 10, yy, pw / 2 - 18, 36, 'ln ln-t'))
                a(rect(cx + 8, yy, pw / 2 - 18, 36, 'ln ln-t'))
            continue
        a(rect(xl + 4, RDC_TOP + 6, xr - xl - 8, GROUND - RDC_TOP - 6, 'ln mask'))
        a(rect(xl + 12, RDC_TOP + 14, xr - xl - 24, 24, 'ln'))
        a(rect(xl + 12, RDC_TOP + 46, xr - xl - 24, GROUND - RDC_TOP - 80, 'ln glass'))
        a(rect(xl + 12, GROUND - 30, xr - xl - 24, 30, 'ln'))
        if kind == 'closed':
            xx = xl + 20
            while xx < xr - 16:
                a(line(xx, RDC_TOP + 50, xx, GROUND - 34, 'ln ln-t'))
                xx += 9
        else:
            a(line((xl + xr) / 2, RDC_TOP + 46, (xl + xr) / 2, GROUND - 30, 'ln ln-t'))
    # devanture active : fond éclairé, intérieur, enseigne, par activité
    lit, frame, _, _, (gl_t, gl_b, door_w) = devanture_parts(active, L, R, '')
    body, litr = lit.split('/>', 1)[0] + '/>', lit.split('/>', 1)[1]
    a(body)
    a(rect(L + 16, gl_t, R - L - 32, gl_b - gl_t, 'glass'))
    a(f'<g class="lit-g">{litr}</g>')
    a(f'<path class="spill" d="M{f(L+16)} {f(GROUND)} L{f(R-16)} {f(GROUND)} L{f(R+60)} {f(GROUND+60)} L{f(L-60)} {f(GROUND+60)} Z" fill="url(#{uid}-spill)"/>')
    for act, label, sign in ACTS:
        inner = interior(act, L + 16, R - 16, gl_t + 4, gl_b)
        a(f'<g class="act act-{act}" data-act="{act}"><g clip-path="url(#{uid}-glass)">{inner}</g></g>')
    a(frame)
    for act, label, sign in ACTS:
        extra = (awning(L, R) + terrace([L + 92, R - 92])) if act == 'restaurant' else ''
        a(f'<g class="act act-{act}">{extra}<text class="sign" x="{f(c)}" y="{f(RDC_TOP+18)}" text-anchor="middle">{sign}</text></g>')
    a('</g>')
    # trottoir, bordure, chaussée
    a(line(0, GROUND, W, GROUND, 'ln ln-b'))
    a(line(0, GROUND + 34, W, GROUND + 34, 'ln'))
    a(line(0, GROUND + 38, W, GROUND + 38, 'ln ln-t'))
    # annotations sourcées
    a('<g class="anns">')
    # enseigne
    sx, sy = R - 30, RDC_TOP + 8
    a(path(f'M{f(sx)} {f(sy)} L{f(sx+60)} {f(sy-70)} H{f(sx+90)}', 'lead'))
    a(circle(sx, sy, 3, 'dot'))
    a(ann_block(sx + 96, sy - 74, "Enseigne : autorisation du maire, 2 mois", "Code de l'environnement, art. R581-13"))
    # porte
    dx = c
    a(line(dx - door_w / 2 + 6, GROUND + 18, dx + door_w / 2 - 6, GROUND + 18, 'dim'))
    a(line(dx - door_w / 2 + 6, GROUND + 12, dx - door_w / 2 + 6, GROUND + 24, 'dim'))
    a(line(dx + door_w / 2 - 6, GROUND + 12, dx + door_w / 2 - 6, GROUND + 24, 'dim'))
    a(path(f'M{f(dx+door_w/2)} {f(GROUND+18)} L{f(dx+150)} {f(GROUND+18)}', 'lead'))
    a(ann_block(dx + 156, GROUND + 14, "Dégagement : 0,90 m sous 20 personnes", "Règlement de sécurité, art. PE 11"))
    # plan de façade (devanture)
    px, py = L - 2, RDC_TOP + 60
    a(circle(px, py, 3, 'dot'))
    a(path(f'M{f(px)} {f(py)} L{f(px-60)} {f(py-150)} H{f(px-96)}', 'lead'))
    a(ann_block(px - 102, py - 154, "Devanture en applique ou retrait de 10 à 20 cm", "PLU de Paris, art. UG.2.1.4", 'end'))
    a('</g>')
    # annotations propres au restaurant
    a('<g class="anns act act-restaurant">')
    kx = R - 70
    a(path(f'M{f(kx)} {f(gl_t+20)} V{f(F1_TOP-30)}', 'lead lead-duct'))
    a(path(f'M{f(kx-6)} {f(F1_TOP-22)} L{f(kx)} {f(F1_TOP-34)} L{f(kx+6)} {f(F1_TOP-22)}', 'lead'))
    a(ann_block(kx + 12, F1_TOP - 12, "Air de cuisine rejeté à 8 m au moins de toute fenêtre", "Règlement sanitaire de Paris, art. 63-1"))
    a(ann_block(L - 160, GROUND + 58, "Terrasse : autorisation de la Ville", "Règlement des étalages et terrasses (2021)"))
    a('</g>')
    # échelle
    sbx, sby = 40, H - 26
    a(f'<g class="scale">{line(sbx, sby, sbx + 5 * M, sby, "dim")}')
    for k, lab in ((0, '0'), (1, '1'), (2, '2'), (5, '5 m')):
        a(line(sbx + k * M, sby - 5, sbx + k * M, sby + 5, 'dim'))
        a(f'<text class="ann" x="{f(sbx + k * M)}" y="{f(sby - 10)}" text-anchor="middle">{lab}</text>')
    a(f'<text class="ann" x="{f(W - 40)}" y="{f(H - 20)}" text-anchor="end">Élévation sur rue, dessin d\'illustration</text></g>')
    a('</svg>')
    return ''.join(o)


def devanture(act, uid):
    """Vignette : la devanture seule, éclairée."""
    L, R = 30, 538
    W = 568
    oy = RDC_TOP - 30
    H = GROUND + 10 - oy
    lit, frame, inner, _, (gl_t, gl_b, door_w) = devanture_parts(act, L, R, '')
    sign = dict((a, s) for a, _, s in ACTS)[act]
    extra = (awning(L, R) + terrace([])) if act == 'restaurant' else ''
    return (f'<svg class="mini" viewBox="0 {oy} {W} {H}" aria-hidden="true" focusable="false">'
            f'<defs><clipPath id="{uid}-c"><rect x="{L+16}" y="{f(gl_t)}" width="{R-L-32}" height="{f(gl_b-gl_t)}"/></clipPath></defs>'
            f'{lit.split("/>",1)[0]}/>{rect(L+16, gl_t, R-L-32, gl_b-gl_t, "glass")}<g class="lit-g">{lit.split("/>",1)[1]}</g>'
            f'<g clip-path="url(#{uid}-c)">{inner}</g>{frame}{extra}'
            f'<text class="sign" x="{f((L+R)/2)}" y="{f(RDC_TOP+17)}" text-anchor="middle">{sign}</text>'
            f'{line(0, GROUND, W, GROUND, "ln ln-b")}</svg>')


# ---------------------------------------------------------------- plan du local
CHECKS = [
    # n, x, y, titre court (repère du plan)
    (1, 400, 300, "Destination et bail"),
    (2, 240, 498, "Linéaire protégé"),
    (3, 660, 50, "Extraction"),
    (4, 168, 420, "Puissance électrique"),
    (5, 400, 470, "Entrée accessible"),
    (6, 532, 262, "Sous-sol et sorties"),
    (7, 160, 136, "Réserve et livraisons"),
    (8, 540, 498, "Façade et enseigne"),
    (9, 92, 300, "Copropriété"),
]


def plan_local(uid='plan'):
    W, H = 800, 560
    o = []
    a = o.append
    a(f'<svg class="plan" viewBox="0 0 {W} {H}" role="img" aria-labelledby="{uid}-t {uid}-d">')
    a(f'<title id="{uid}-t">Plan d\'un local commercial en rez-de-chaussée</title>')
    a(f'<desc id="{uid}-d">Plan d\'illustration : salle de vente sur rue, réserve et sanitaires au fond, escalier vers le sous-sol, cour de l\'immeuble, entrée commune. Neuf repères situent les points à vérifier avant de signer un bail.</desc>')
    a('<defs><pattern id="%s-h" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="6" class="hatch"/></pattern></defs>' % uid)
    wall = 'wall'
    # murs extérieurs (poché)
    a(path('M120 104 H692 V470 H586 V482 H704 V92 H108 V482 H214 V470 H120 Z', wall))
    # mur mitoyen gauche + entrée d'immeuble (couloir commun)
    a(path('M40 92 H108 V104 H52 V470 H96 V482 H40 Z', wall))
    a(f'<rect x="52" y="104" width="56" height="366" fill="url(#{uid}-h)" class="common"/>')
    a('<text class="pl-t" x="80" y="200" text-anchor="middle" transform="rotate(-90 80 200)">Entrée de l\'immeuble</text>')
    # cour au fond
    a(rect(108, 20, 596, 72, 'ln ln-t'))
    a('<text class="pl-t" x="300" y="62">Cour de l\'immeuble</text>')
    # cloison réserve / sanitaires
    a(path('M120 210 H330 M370 210 H520 M520 104 V210 M440 104 V210', 'ln ln-b'))
    a('<text class="pl-t" x="226" y="164" text-anchor="middle">Réserve</text>')
    a('<text class="pl-t" x="480" y="164" text-anchor="middle">Sanitaires</text>')
    a('<text class="pl-t" x="606" y="150" text-anchor="middle">Office</text>')
    a(path('M330 210 A40 40 0 0 1 370 170', 'ln ln-t'))
    # porte de service vers la cour
    a(path('M640 104 V92', 'ln'))
    a(path('M600 104 A40 40 0 0 1 640 64', 'ln ln-t'))
    # escalier vers sous-sol
    a(rect(560, 228, 92, 120, 'ln'))
    for k in range(1, 8):
        a(line(560, 228 + k * 15, 652, 228 + k * 15, 'ln ln-t'))
    a(path('M606 336 V244 M598 254 L606 240 L614 254', 'ln'))
    a('<text class="pl-t" x="606" y="368" text-anchor="middle">Sous-sol</text>')
    # caisse et mobilier de vente (pointillé)
    a(rect(160, 250, 120, 40, 'ln ln-d'))
    a('<text class="pl-t" x="220" y="275" text-anchor="middle">Caisse</text>')
    a(rect(330, 260, 150, 80, 'ln ln-d'))
    a(rect(140, 330, 18, 120, 'ln ln-d'))
    a('<text class="pl-t pl-big" x="400" y="410" text-anchor="middle">Salle de vente</text>')
    # tableau électrique
    a(rect(124, 410, 12, 22, 'ln ln-b'))
    # façade : vitrines et porte
    a(path('M214 476 H372 M428 476 H586', 'ln ln-b'))
    a(path('M214 470 V482 M586 470 V482', 'ln'))
    a(path('M372 476 V470 M428 476 V470 M372 476 A56 56 0 0 0 428 420', 'ln ln-t'))
    # gaine d'extraction (pointillé vers la cour)
    a(rect(600, 40, 20, 20, 'ln ln-b'))
    a(path('M610 60 V104', 'ln ln-d'))
    # rue
    a(line(0, 520, W, 520, 'ln'))
    a('<text class="pl-t" x="700" y="546" text-anchor="end">Rue</text>')
    # repères
    for n, x, y, t in CHECKS:
        a(f'<g class="pin" data-pin="{n}"><circle cx="{x}" cy="{y}" r="15"/><text x="{x}" y="{y+5}" text-anchor="middle">{n}</text></g>')
    # nord et échelle
    a('<g class="scale"><line class="dim" x1="40" y1="540" x2="200" y2="540"/><line class="dim" x1="40" y1="534" x2="40" y2="546"/><line class="dim" x1="120" y1="534" x2="120" y2="546"/><line class="dim" x1="200" y1="534" x2="200" y2="546"/>'
      '<text class="ann" x="40" y="530" text-anchor="middle">0</text><text class="ann" x="120" y="530" text-anchor="middle">2</text><text class="ann" x="200" y="530" text-anchor="middle">4 m</text></g>')
    a('</svg>')
    return ''.join(o)
