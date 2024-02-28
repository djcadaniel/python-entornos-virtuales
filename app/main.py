import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./data.csv')
  data = list(filter( lambda item: item['Nombre de la campaÃ±a'] == 'WS.24.01.V2', data))

  publications = list(map(lambda x: x['Nombre de la campaÃ±a'], data))
  impresiones = list(map(lambda x: x['Impresiones'], data))
  charts.generate_pie_chart(publications, impresiones)  
  
  #otro grafico
  
  camp = input('Ingresa nombre de campaña: ')
  result = utils.publications_by_name_camp(data, camp)
  
  if len(result) > 0:
    camp = result[0]
    labels, values = utils.get_publications(camp)
    charts.generate_bar_chart(camp['Nombre de la campaÃ±a'], labels, values)
  
if __name__ == '__main__':
  run()