"""
Utilitários para manipulação de DateTime
"""

from datetime import datetime, timedelta
from typing import Union
import logging

logger = logging.getLogger(__name__)

def safe_datetime_conversion(date_value: Union[str, datetime]) -> datetime:
    """
    Converte string para datetime de forma segura
    
    Args:
        date_value: String ou datetime a ser convertido
        
    Returns:
        datetime: Objeto datetime válido
    """
    if isinstance(date_value, datetime):
        return date_value
    
    if isinstance(date_value, str):
        # Formatos comuns de datetime
        formats = [
            "%Y-%m-%dT%H:%M:%S.%f",      # ISO com microssegundos
            "%Y-%m-%dT%H:%M:%S",         # ISO sem microssegundos
            "%Y-%m-%d %H:%M:%S.%f",      # Formato padrão com microssegundos
            "%Y-%m-%d %H:%M:%S",         # Formato padrão sem microssegundos
            "%Y-%m-%d",                  # Apenas data
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_value, fmt)
            except ValueError:
                continue
        
        # Se nenhum formato funcionou, log do erro e retorna fallback
        logger.warning(f"Falha ao converter datetime: '{date_value}'. Usando fallback.")
        return datetime.now()
    
    # Se não é string nem datetime, usar fallback
    logger.error(f"Tipo inválido para conversão datetime: {type(date_value)}. Usando fallback.")
    return datetime.now()

def calculate_time_remaining(end_date: Union[str, datetime], now: datetime = None) -> timedelta:
    """
    Calcula tempo restante de forma segura
    
    Args:
        end_date: Data final (string ou datetime)
        now: Data atual (opcional, usa datetime.now() se não fornecido)
        
    Returns:
        timedelta: Tempo restante (0 se já passou)
    """
    if now is None:
        now = datetime.now()
    
    # Converter end_date para datetime
    end_datetime = safe_datetime_conversion(end_date)
    
    # Calcular diferença
    time_left = end_datetime - now if end_datetime > now else timedelta(0)
    
    return time_left

def format_time_remaining(time_left: timedelta) -> str:
    """
    Formata tempo restante em string legível
    
    Args:
        time_left: Tempo restante
        
    Returns:
        str: Tempo formatado (ex: "5d, 3h, 45min")
    """
    if time_left.total_seconds() <= 0:
        return "Tempo esgotado!"
    
    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    if days > 0:
        return f"{days}d, {hours}h, {minutes}min"
    elif hours > 0:
        return f"{hours}h, {minutes}min"
    else:
        return f"{minutes}min"

