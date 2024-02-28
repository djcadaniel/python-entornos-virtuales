def get_publications(camp_dict):
  publication_dict = {
    '2024': float(camp_dict['Importe gastado (USD)']),
    '2022': float(camp_dict['Importe gastado (USD)']),
    '2020': float(camp_dict['Importe gastado (USD)']),
    '2015': float(camp_dict['Importe gastado (USD)']),
    '2010': float(camp_dict['Importe gastado (USD)']),
    '2000': float(camp_dict['Importe gastado (USD)']),
    '1990': float(camp_dict['Importe gastado (USD)']),
    '1980': float(camp_dict['Importe gastado (USD)']),
    '1970': float(camp_dict['Importe gastado (USD)']),
  }
  labels= publication_dict.keys()
  values= publication_dict.values()
  return labels, values

def publications_by_name_camp(data, name_camp):
  result = list(filter(lambda item: item['Nombre de la campaÃ±a'] == name_camp, data))
  return result