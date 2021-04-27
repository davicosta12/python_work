cria_linha_gota(screen, settings, gota, gotas)

def cria_linha_gota(screen, settings, gota, gotas):
    if gota.VerificaOndeAgotaEncosta():
        gota = Gota(screen, settings)
        avaliando_space_x = settings.screen_width - gota.rect.width
        number_gotas = int(avaliando_space_x / (2 * gota.rect.width))

        for number_gota in range(number_gotas):
            gota = Gota(screen, settings)
            position_x = gota.rect.width + (2 * gota.rect.width) * number_gota
            gota.rect.x = position_x
            gotas.add(gota)