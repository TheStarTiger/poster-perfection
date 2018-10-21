import colormath
from colormath.color_objects import LabColor, sRGBColor, HSLColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976, delta_e_cmc, delta_e_cie2000
color1 = sRGBColor(130, 0, 255)
color2 = sRGBColor(90, 91, 0)
color3 = sRGBColor(0, 244, 61)
color4 = sRGBColor(139, 37, 255)
color5 = sRGBColor(162, 59, 0)
color6 = sRGBColor(97, 82, 0)
color7 = sRGBColor(255, 221, 0)
color8 = sRGBColor(252, 255, 0)
color9 = sRGBColor(255, 255, 255)
color10 = sRGBColor(255, 132, 238)
color1 = convert_color(color1, LabColor)
color2 = convert_color(color2, LabColor)
delta_1 = delta_e_cmc(color1, color2, 1, 1)
delta_2 = delta_e_cmc(color1, convert_color(color7, LabColor))
delta_3 = delta_e_cmc(color1, convert_color(color8, LabColor))
delta_4 = delta_e_cmc(color1, convert_color(color9, LabColor))
delta_5 = delta_e_cmc(color1, convert_color(color10, LabColor))
# print(delta_1)
# print(delta_2)
# print(delta_3)
# print(delta_4)
# print(delta_5)

# Note, close but not quite, according to the data before us


def colblind_convert_deu(rgb):
    r = (0.625*rgb.rgb_r) + (0.7*rgb.rgb_g) + (0*rgb.rgb_b)
    g = (0.375*rgb.rgb_r) + (0.3*rgb.rgb_g) + (0.3*rgb.rgb_b)
    b = (0.0*rgb.rgb_r) + (0*rgb.rgb_g) + (0.7*rgb.rgb_b)
    return sRGBColor(r, g, b)


def colblind_convert_deuly(rgb):
    r = (0.8*rgb.rgb_r) + (0.25833*rgb.rgb_g) + (0*rgb.rgb_b)
    g = (0.2*rgb.rgb_r) + (0.74167*rgb.rgb_g) + (0.14167*rgb.rgb_b)
    b = (0.0*rgb.rgb_r) + (0*rgb.rgb_g) + (0.85833*rgb.rgb_b)
    return sRGBColor(r, g, b)


def compliment_rgb(rgb):
    hsl = convert_color(rgb, HSLColor)
    new_h = hsl.hsl_h - 180
    if new_h < 0:
        new_h += 360
    hsl.hsl_h = new_h
    return convert_color(hsl, sRGBColor)


def compliment_hsl(rgb):
    hsl = convert_color(rgb, HSLColor)
    new_h = hsl.hsl_h - 180
    if new_h < 0:
        new_h += 360
    hsl.hsl_h = new_h
    return hsl


def rgb_delta_e_cmc(rgb1, rgb2):
    return delta_e_cmc(convert_color(rgb1, LabColor), convert_color(rgb2, LabColor))


def rgb_delta_e_cie2000(rgb1, rgb2):
    return delta_e_cie2000(convert_color(rgb1, LabColor), convert_color(rgb2, LabColor))


def rough_rgb_hex(hex_str):
    return [int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:], 16)]


def main():
    col1 = sRGBColor(172, 172, 0)
    col2 = colblind_convert_deu(col1)
    col11 = compliment_rgb(col1)
    col21 = colblind_convert_deu(col11)

    print(col2)
    print(col21)
    print(rgb_delta_e_cie2000(col1, col11))
    print(rgb_delta_e_cie2000(col2, col21))
    print(rgb_delta_e_cie2000(sRGBColor(60, 0, 0), sRGBColor(60, 1, 0)))


