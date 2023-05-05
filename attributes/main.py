from attribute_access import AttributeAccess

if __name__ == '__main__':
    MAIN = 'MAIN'

    print(f'{MAIN:20} | creating instance of {AttributeAccess.__name__}')
    m = AttributeAccess()
    print()

    print(f'{MAIN:20} | getting m.prop ...')
    print(f'{MAIN:20} | getting m.prop --> {m.prop = }')
    print()

    print(f'{MAIN:20} |  setting m.prop = "property-value" ...')
    m.prop = 'property-value'
    print()

    print(f'{MAIN:20} | getting m.prop ...')
    print(f'{MAIN:20} | getting m.prop --> {m.prop = }')
    print()

    """
    
    
    
    """
    print(f'{MAIN:20} | getting m.x ...')
    print(f'{MAIN:20} | getting m.x --> {m.x = }')
    print()

    try:
        print(f'{MAIN:20} | trying to get m["x"] ...')
        print(f'{MAIN:20} | {m["x"] = }')
        print()
    except KeyError as ke:
        print(f'{MAIN:20} |  {ke!r}')
        print()

    print(f'{MAIN:20} |  setting m.x = 0 ...')
    m.x = 0
    print()

    print(f'{MAIN:20} |  get m.x ...')
    print(f'{MAIN:20} |  {m.x = }')
    print()

    print(f'{MAIN:20} |  getting m.__dict__ ...')
    print(f'{MAIN:20} |  {m.__dict__ = }')
    print()

    print(f'{MAIN:20} |  getting m["x"] ...')
    print(f'{MAIN:20} |  {m["x"] = }')
    print()

    print('MAIN |  setting m["x"] = 1 ...')
    m["x"] = 1
    print()

    print(f'{MAIN:20} | trying to get m["x"] ...')
    print(f'{MAIN:20} | {m["x"] = }')
    print()

    print(f'{MAIN:20} |  getting m.__dict__ ...')
    print(f'{MAIN:20} |  {m.__dict__ = }')
    print()
