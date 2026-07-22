#include <iostream>
#include <vector>
#include <memory>
#include <string>
#include <map>

class Bateria{
    private:
        int temperatura;
        int nivelCarga;
        int ciclosDeCarga;
    public:
        Bateria():temperatura(25),nivelCarga(100),ciclosDeCarga(0){}
        void usar()
        {
            nivelCarga = (nivelCarga > 0) ? nivelCarga-5:0;
        }

        void cargar()
        {
            nivelCarga = (nivelCarga < 100) ? nivelCarga+10:100;
            ciclosDeCarga++;
        }
        void mostrarEstado()
        {
            std::cout << "El nivel de carga es: " << nivelCarga 
                  << " | Temperatura: " << temperatura 
                  << "°C | Ciclos de carga: " << ciclosDeCarga 
                  << std::endl;  
        }
        int getNivel()
        {
            return nivelCarga;
        }
};

int main()
{
    Bateria miBateria;
    
    std::cout << "=== ESTADO INICIAL ===" << std::endl;
    miBateria.mostrarEstado();
    
    std::cout << "\n=== USANDO BATERÍA ===" << std::endl;
    while (miBateria.getNivel() != 20)
    {    
     miBateria.usar();
    }
    miBateria.mostrarEstado();
    
    std::cout << "\n=== CARGANDO BATERÍA ===" << std::endl;
    miBateria.cargar();
    miBateria.mostrarEstado();
    
    std::cout << "\n=== NIVEL ACTUAL ===" << std::endl;
    std::cout << "Nivel: " << miBateria.getNivel() << "%" << std::endl;
    
    return 0;
}