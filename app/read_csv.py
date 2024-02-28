import csv

def read_csv(path):
  with open(path, 'r') as cvfile:
    reader = csv.reader(cvfile, delimiter=',')
    header = next(reader)
    data = []
    # print(header)
    for row in reader:
      iterable = zip(header, row)
      # print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./data.csv')
  print(data)