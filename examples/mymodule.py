import argschema

class MySchema(argschema.ArgSchema):
    a = argschema.fields.Int(default = 42, 
                            metadata = {'description':'my first parameter'})
                            
if __name__ == '__main__':
    mod = argschema.ArgSchemaParser(schema_type=MySchema)
    mod.run()
    