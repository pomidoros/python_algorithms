MetaClass = type.__new__('MetaClass', (object, ), {})
Class = MetaClass('Class', (object, ), {'a': 10})
