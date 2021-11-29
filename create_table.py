from psycopg2 import connect

#with connect(host= '::', port= '8001', user= 'postgres', database= 'todos', password= 'secret') as con:
#    cur = con.cursor()
#    cur.execute('SELECT version()')
#
#    version = cur.fetchone()[0]
#    print(version)

def setNames():
    foo = input('# ')
    if foo == '\q':
        return (False,)
    if len(foo.strip().split()) != 2:
        return (False,)
    return (foo.strip().split(),)

def main():
    #print(setNames()[0])
    #while(setNames()[0]):
    #   print('mission complete')
    with connect(host='::', port= '8001', user= 'postgres', database= 'todos', password= 'secret') as conn:
        feedQuery = conn.cursor()
        print('-'*128)
        feedQuery.execute('SELECT version()')
        print(feedQuery.fetchone()[0])
        print('-'*128)
        
        feedQuery.execute("DROP TABLE IF EXISTS cars")
        feedQuery.execute("CREATE TABLE cars(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")
        state = True
        print('Insert model car and price.')
        while(state):
            try:
                col1, col2 = setNames()[0]
                if col1 is False:
                    break
                col2 = int(col2)
                feedQuery.execute("INSERT INTO cars(name, price) VALUES('%s', %d)"%(col1, col2))
            except Exception:
                break

if __name__ == "__main__":
    main()
