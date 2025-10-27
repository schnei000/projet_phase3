#  
from lib.models import Session, init_db
from lib.cli import main   

if __name__ == '__main__':
    init_db()              
    main()