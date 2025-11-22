# gestor-recetas-python/models/receta.py

from __future__ import annotations
from dataclasses import dataclass, field

from models.ingrediente import Ingrediente

@dataclass
class Receta:
    nombre: str
    ingredientes: list[Ingrediente] = field(default_factory=list)
    pasos: list[str] = field(default_factory=list)
    
    def añadir_ingrediente(self, ingrediente: Ingrediente) -> Ingrediente:
        self.ingredientes.append(ingrediente)
        return ingrediente
    
    def añadir_paso(self, paso: str) -> str:
        self.pasos.append(paso)
        return paso
    
    def __repr__(self) -> str:
        lineas_ingredientes = '\n'.join(
            f' - {ing.cantidad} {ing.unidad} de {ing.nombre}'
            for ing in self.ingredientes
        ) or " (sin ingredientes)"
        
        lineas_pasos = '\n'.join(
            f" {i}. {paso}"
            for i, paso in enumerate(self.pasos, start=1)
        ) or " (sin pasos)"
        
        return (
            f"Receta: {self.nombre}\n"
            f"Ingredientes:\n{lineas_ingredientes}\n"
            f"Pasos:\n{lineas_pasos}"
        )
        