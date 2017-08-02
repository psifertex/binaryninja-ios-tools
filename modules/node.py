from enum import Enum

Kind = Enum('Kind', 'ALLOCATOR ARGUMENT_TUPLE ASSOCIATED_TYPE_METADATA_ACCESSOR ASSOCIATED_TYPE_WITNESS_TABLE_ACCESSOR BOUND_GENERIC_CLASS BOUND_GENERIC_ENUM BOUND_GENERIC_STRUCTURE CLASS CONSTRUCTOR DEALLOCATOR DEFAULT_ARGUMENT_INITIALIZER DEPENDENT_ASSOCIATED_TYPE_REF DEPENDENT_GENERIC_CONFORMANCE_REQUIREMENT DEPENDENT_GENERIC_LAYOUT_REQUIREMENT DEPENDENT_GENERIC_PARAM_COUNT DEPENDENT_GENERIC_PARAM_TYPE DEPENDENT_GENERIC_SAME_TYPE_REQUIREMENT DEPENDENT_GENERIC_TYPE DEPENDENT_GENERIC_SIGNATURE DEPENDENT_MEMBER_TYPE DEPENDENT_PSEUDOGENERIC_SIGNATURE DESCTRUCTOR DID_SET DIRECT_METHOD_REFERENCE_ATTRIBUTE DYNAMIC_ATTRIBUTE ENUM EXPLICIT_CLOSURE EXTENSION FIELD_OFFSET FULL_TYPE_METADATA FUNCTION FUNCTION_SIGNATURE_SPECIALIZATION FUNCTION_SIGNATURE_SPECIALIZATION_PARAM FUNCTION_SIGNATURE_SPECIALIZATION_PARAM_KIND FUNCTION_TYPE GENERIC_PROTOCOL_WITNESS_TABLE GENERIC_PROTOCOL_WITNESS_TABLE_INSTANTIATION_FUNCTION GENERIC_TYPE_METADATA_PATTERN GENERIC_SPECIALIZATION GENERIC_SPECIALIZATION_NOT_RE_ABSTRACTED GENERIC_SPECIALIZATION_PARAM GETTER GLOBAL GLOBAL_GETTER IDENTIFIER IMPLICIT_CLOSURE IN_OUT INDEX INITIALIZER IVAR_DESTROYER IVAR_INITIALIZER LAZY_PROTOCOL_WITNESS_TABLE_ACCESSOR LOCAL_DECL_NAME MATERIALIZE_FOR_SET METACLASS MODULE NATIVE_OWNING_MUTABLE_ADDRESSOR NATIVE_PINNING_MUTABLE_ADDRESSOR NOMINAL_TYPE_DESCRIPTOR NON_OBJC_ATTRIBUTE NUMBER OBJC_ATTRIBUTE OWNING_MUTABLE_ADDRESSSOR PRIVATE_DECL_NAME PROTOCOL PROTOCOL_CONFORMANCE PROTOCOL_DESCRIPTOR PROTOCOL_LIST PROTOCOL_WITNESS PROTOCOL_WITNESS_TABLE PROTOCOL_WITNESS_TABLE_ACCESSOR SETTER SPECIALIZATION_IS_FRAGILE SPECIALIZATION_PASS_ID STATIC STRUCTURE SUBSCRIPT REABSTRACTION_THUNK REABSTRACTION_THUNK_HELPER RETURN_TYPE SUFFIX THROWS_ANNOTATION TUPLE TUPLE_ELEMENT TUPLE_ELEMENT_NAME TYPE TYPE_LIST TYPE_MANGLING TYPE_METADATA TYPE_METADATA_ACCESS_FUNCTION TYPE_METADATA_LAZY_CACHE UNCURRIED_FUNCTION_TYPE UNSAFE_MUTABLE_ADDRESSOR VALUE_WITNESS_TABLE VARIABLE VARIADIC_MARKER VTABLE_ATTRIBUTE WILL_SET')

class Node():
    def __init__(self, kind, text="", index=-1):
        self.kind = kind
        self.children = []
        self.text = text
        if index >= 0:
            self.index = index

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.text != "":
            if len(self.children) == 0:
                return "{{{}({})}}".format(self.kind, self.text, self.children)
            return "{{{}({}) children: {}}}".format(self.kind, self.text, self.children)
        return "{{{} children: {}}}".format(self.kind, self.children)

    def getNumChildren(self):
        return len(self.children)

    def getChild(self, n):
        return self.children[n]

    def addChild(self, child):
        self.children.append(child)
        return self

    def reverseChildren(self, starting_at=0):
        self.children = self.children[:starting_at] + self.children[starting_at:][::-1]
