import Moduls.Exercici1 as E1
import Moduls.Exercici2 as E2
import Moduls.Exercici3 as E3
import Moduls.Exercici4 as E4
import Moduls.Exercici5 as E5
import Moduls.Exercici6 as E6


def practica_sencera(auto: bool = True) -> None:
    firearm_checks = E1.exercici1(auto)
    firearm_checks = E2.exercici2(firearm_checks, auto)
    firearm_checks = E3.exercici3(firearm_checks, auto)
    E4.exercici4(firearm_checks, auto)
    firearm_checks = E5.exercici5(firearm_checks, auto)
    E6.exercici6(firearm_checks, auto)


def main() -> None:
    print("Executar tota la practica per defecte:")
    practica_sencera()
    # Triar quina funció volem executar
    while True:
        defecte = input("Vols tornar a executar tota la practica per defecte, executar les funcions una a una o "
                        "sortir?\n1: Executar les funcions una a una \n0: Executar-les totes per defecte\nPer sortir "
                        "pitja qualsevol lletra del teclat\n")
        if defecte == "0":
            print("Executar tota la practica per defecte:")
            practica_sencera()
        elif defecte == "1":
            print("Executant la practica funcio per funcio:")
            practica_sencera(False)
        else:
            break


if __name__ == '__main__':
    main()
