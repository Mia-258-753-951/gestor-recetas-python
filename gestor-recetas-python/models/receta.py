# gestor-recetas-python/models/receta.py

from __future__ import annotations
from dataclasses import dataclass, field

from .ingrediente import Ingrediente

@dataclass
class Receta:
    nombre: str
    ingredientes: list[Ingrediente] = field(default_factory=list)
    pasos: list[str | None] = field(default_factory=list)
    
    def añadir_ingrediente(self, ingrediente: Ingrediente) -> Ingrediente:
        self.ingredientes.append(ingrediente)
        return ingrediente
    
    def añadir_paso(self, paso: str) -> str:
        self.pasos.append(paso)
        return paso
    
    def __repr__(self) -> str:
        return (
                f'- Receta: {self.nombre}\n'
                f'- Ingredientes: {[ingrediente.nombre for ingrediente in self.ingredientes]}\n'
                f'- Pasos: {self.pasos}\n'
                )
        