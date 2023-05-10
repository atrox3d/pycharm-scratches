"""
this first import line unleashes the following events:

1) imports attribute_access
    2) imports property_access
        3) defines PropertyAccess
    4) defines AttributeAccess
        5) declares prop as:
            PropertyAccess instance
            AttributeAccess class variable
            6) calls PropertyAccess.__set_name__(
                                            self,   # PropertyAccess instance
                                            owner,  # AttributeAccess class
                                            name    # name: "prop"
                                    )

"""
from classes.attribute_access import AttributeAccess

if __name__ == '__main__':
    MAIN = 'MAIN'

    header = f'{MAIN:25}'
    print(f'{header} | m = AttributeAccess()')
    m = AttributeAccess()
    print()

    print(f'{header} | getting m.prop ...')
    """
    1) AttributeAccess.__getattribute__(                                                      
                            self,               # AttributeAccess instance      
                            item                # 'prop'                                                                       
                    )                                                                                     
        2) PropertyAccess.__get__(                                                                
                                self,           # PropertyAccess instance        
                                instance,       # AttributeAccess instance  
                                owner           # class AttributeAccess                          
                        )                                                                                     
            3) PropertyAccess.__getattribute__(                                                       
                                    self,       # PropertyAccess instance        
                                    item,       # 'value'                                                                      
                                 )
                # prop.value does not yet exist at this time                                                                                     
                4) PropertyAccess.__getattr__(                                                            
                                    self,       # PropertyAccess instance        
                                    item        # 'value',                                                                      
                                 )                                                                                     
    """
    print(f'{header} | getting m.prop --> {m.prop = }')
    print()

    print(f'{header} |  setting m.prop = "property-value" ...')
    """
    1) AttributeAccess.__setattr__(                                                            
                            self,               # AttributeAccess instance       
                            key,                # 'prop'                                                                         
                            value               # 'property-value'                                                             
                         )                                                                                      
        2) PropertyAccess.__set__(                                                                 
                                self,           # PropertyAccess instance         
                                instance,       # AttributeAccess instance   
                                value           # 'property-value'                                                             
                             )                                                                                      
            3) PropertyAccess.__setattr__(                                                             
                                    self,       # PropertyAccess instance         
                                    key,        # 'value'                                                                        
                                    value       # 'property-value'                                                                 
                                )    
    """
    m.prop = 'property-value'
    print()

    print(f'{header} | getting m.prop ...')
    """
    same as before, this time prop.value exists
    so PropertyAccess.__getattr__ in NOT called
    """
    print(f'{header} | getting m.prop --> {m.prop = }')
    print()

    print(f'{header} | getting m.x ...')
    print(f'{header} | getting m.x --> {m.x = }')
    print()

    try:
        print(f'{header} | trying to get m["x"] ...')
        print(f'{header} | {m["x"] = }')
        print()
    except KeyError as ke:
        print(f'{header} |  {ke!r}')
        print()

    print(f'{header} |  setting m.x = 0 ...')
    m.x = 0
    print()

    print(f'{header} |  get m.x ...')
    print(f'{header} |  {m.x = }')
    print()

    print(f'{header} |  getting m.__dict__ ...')
    print(f'{header} |  {m.__dict__ = }')
    print()

    print(f'{header} |  getting m["x"] ...')
    print(f'{header} |  {m["x"] = }')
    print()

    print('MAIN |  setting m["x"] = 1 ...')
    m["x"] = 1
    print()

    print(f'{header} | trying to get m["x"] ...')
    print(f'{header} | {m["x"] = }')
    print()

    print(f'{header} |  getting m.__dict__ ...')
    print(f'{header} |  {m.__dict__ = }')
    print()
