"""A basic (two-function) API written using Hug"""
import hug
import json

from bgs_etl import get_connection, get_rows, BGSPROD
from bgs_etl.row_factories import dict_rowfactory


@hug.get('/borehole/{borehole_number}')
def borehole_by_number(borehole_number: hug.types.number):
    """Get borehole data."""
    sql = """
        SELECT * FROM BGS.SOBI
        WHERE NUMB = :borehole_number
        """
    params = {"borehole_number": borehole_number}

    with get_connection(BGSPROD, 'ORACLE_PASSWORD') as conn:
        result = get_rows(sql, conn, parameters=params,
                          row_factory=dict_rowfactory)

    return json.dumps(result, default=str)
