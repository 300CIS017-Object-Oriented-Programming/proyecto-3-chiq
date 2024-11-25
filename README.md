[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9bKkctvo)
# snies_proyecto_3
Proyecto_3



```mermaid
classDiagram
direction BT

class Persona{
  -int identificacion
  -string nombre
  -string sexo
  -int puntaje

}

class Huesped{
  
}

class Propietario{
  -bool recibirHuesped
}

class Hogar{
  -string direccion
  -int numeroCamasDisponibles
  -bool alojarBebes
  -string descripcionHogar
  
}

Propietario <|-- Hogar
Persona <|-- Huesped
Persona <|-- Propietario



```
