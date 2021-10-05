#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib.colors import cnames


def list_to_dict(some_list: list) -> dict:
    some_dict = {}
    for element in some_list:
        some_dict[element] = some_list.index(element)
    # TODO: Transformer la liste en dictionnaire, les éléments de la liste deviennent les clés et leur index deviennent les valeurs

    return some_dict
    # return {value : index for index, value in enumerate(some_list)}


def color_name_to_hex(colors: list) -> list:
    color_list = []
    for color in colors:
        color_tuple = (color, cnames.get(color))
        color_list.append(color_tuple)
    # TODO: Trouver la valeur hex de chaque couleur dans la liste et créer une liste de tupple où le premier élément est le nom de la couleur et le deuxième est la valeur hex

    return color_list
    # return [(color, cnames[color]) for color in colors]


def create_list() -> list:
    fuckton_of_numbers = []
    n = 0
    while len(fuckton_of_numbers) <= 10000:
        if n < 15 or n > 350:
            fuckton_of_numbers.append(n)
        n += 1
    # TODO: Créer une liste des 10 000 premiers entiers positif, sauf pour les entiers de 15 à 350

    return fuckton_of_numbers
    # return [i for i in range(10000) if not(15 <= i <= 350)]


def compute_mse(model_dict: dict) -> dict:
    mse_dict = {}
    for model in model_dict:
        mse = 0
        for i in range(len(model_dict[model])):
            mse += (model_dict[model][i][0] - model_dict[model][i][1]) ** 2
        mse_dict[model] = round((1 / len(model_dict[model])) * mse, 1)
    # TODO: Calculer l'erreur quadratique moyen pour chaque modèle. Retourner un dictionnaire contenant les MSE.

    return mse_dict
    # return {model: sum([(y - y_pred)**2 for y, y_pred in results]) / len(results) for model, results in model_dict.items()}


def main() -> None:
    some_list = ["a", "b", "z", "patate"]
    print(f"La liste suivante {some_list} est transformée en dictionnaire: {list_to_dict(some_list)}")

    colors = ["blue", "red", "green", "yellow", "black", "white"]
    print(f"La valeur hex associée aux couleurs est: {color_name_to_hex(colors)}")

    print(f"La liste des 10000 entiers est: {create_list()}")

    model_dict = {"LR": [(90, 92), (96, 100), (20, 25), (21, -2), (3, -20)],
                  "DNN": [(100, 101), (50, 50), (1,2), (-10, -12), (-1, 7)],
                  "RF": [(10, 19), (56, 70), (1, 9), (-100, -12), (-11, 7)]}
    print(f"Le mse des différents modèles est: {compute_mse(model_dict)}")


if __name__ == '__main__':
    main()
