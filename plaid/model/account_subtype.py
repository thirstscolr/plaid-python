"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.474.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from plaid.exceptions import ApiAttributeError



class AccountSubtype(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'None': None,
            '401A': "401a",
            '401K': "401k",
            '403B': "403B",
            '457B': "457b",
            '529': "529",
            'BROKERAGE': "brokerage",
            'CASH_ISA': "cash isa",
            'CRYPTO_EXCHANGE': "crypto exchange",
            'EDUCATION_SAVINGS_ACCOUNT': "education savings account",
            'EBT': "ebt",
            'FIXED_ANNUITY': "fixed annuity",
            'GIC': "gic",
            'HEALTH_REIMBURSEMENT_ARRANGEMENT': "health reimbursement arrangement",
            'HSA': "hsa",
            'ISA': "isa",
            'IRA': "ira",
            'LIF': "lif",
            'LIFE_INSURANCE': "life insurance",
            'LIRA': "lira",
            'LRIF': "lrif",
            'LRSP': "lrsp",
            'NON-CUSTODIAL_WALLET': "non-custodial wallet",
            'NON-TAXABLE_BROKERAGE_ACCOUNT': "non-taxable brokerage account",
            'OTHER': "other",
            'OTHER_INSURANCE': "other insurance",
            'OTHER_ANNUITY': "other annuity",
            'PRIF': "prif",
            'RDSP': "rdsp",
            'RESP': "resp",
            'RLIF': "rlif",
            'RRIF': "rrif",
            'PENSION': "pension",
            'PROFIT_SHARING_PLAN': "profit sharing plan",
            'RETIREMENT': "retirement",
            'ROTH': "roth",
            'ROTH_401K': "roth 401k",
            'RRSP': "rrsp",
            'SEP_IRA': "sep ira",
            'SIMPLE_IRA': "simple ira",
            'SIPP': "sipp",
            'STOCK_PLAN': "stock plan",
            'THRIFT_SAVINGS_PLAN': "thrift savings plan",
            'TFSA': "tfsa",
            'TRUST': "trust",
            'UGMA': "ugma",
            'UTMA': "utma",
            'VARIABLE_ANNUITY': "variable annuity",
            'CREDIT_CARD': "credit card",
            'PAYPAL': "paypal",
            'CD': "cd",
            'CHECKING': "checking",
            'SAVINGS': "savings",
            'MONEY_MARKET': "money market",
            'PREPAID': "prepaid",
            'AUTO': "auto",
            'BUSINESS': "business",
            'COMMERCIAL': "commercial",
            'CONSTRUCTION': "construction",
            'CONSUMER': "consumer",
            'HOME_EQUITY': "home equity",
            'LOAN': "loan",
            'MORTGAGE': "mortgage",
            'OVERDRAFT': "overdraft",
            'LINE_OF_CREDIT': "line of credit",
            'STUDENT': "student",
            'CASH_MANAGEMENT': "cash management",
            'KEOGH': "keogh",
            'MUTUAL_FUND': "mutual fund",
            'RECURRING': "recurring",
            'REWARDS': "rewards",
            'SAFE_DEPOSIT': "safe deposit",
            'SARSEP': "sarsep",
            'PAYROLL': "payroll",
            'NULL': "null",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = True

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """AccountSubtype - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): See the [Account type schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full listing of account types and corresponding subtypes.., must be one of ["401a", "401k", "403B", "457b", "529", "brokerage", "cash isa", "crypto exchange", "education savings account", "ebt", "fixed annuity", "gic", "health reimbursement arrangement", "hsa", "isa", "ira", "lif", "life insurance", "lira", "lrif", "lrsp", "non-custodial wallet", "non-taxable brokerage account", "other", "other insurance", "other annuity", "prif", "rdsp", "resp", "rlif", "rrif", "pension", "profit sharing plan", "retirement", "roth", "roth 401k", "rrsp", "sep ira", "simple ira", "sipp", "stock plan", "thrift savings plan", "tfsa", "trust", "ugma", "utma", "variable annuity", "credit card", "paypal", "cd", "checking", "savings", "money market", "prepaid", "auto", "business", "commercial", "construction", "consumer", "home equity", "loan", "mortgage", "overdraft", "line of credit", "student", "cash management", "keogh", "mutual fund", "recurring", "rewards", "safe deposit", "sarsep", "payroll", "null", ]  # noqa: E501

        Keyword Args:
            value (str): See the [Account type schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full listing of account types and corresponding subtypes.., must be one of ["401a", "401k", "403B", "457b", "529", "brokerage", "cash isa", "crypto exchange", "education savings account", "ebt", "fixed annuity", "gic", "health reimbursement arrangement", "hsa", "isa", "ira", "lif", "life insurance", "lira", "lrif", "lrsp", "non-custodial wallet", "non-taxable brokerage account", "other", "other insurance", "other annuity", "prif", "rdsp", "resp", "rlif", "rrif", "pension", "profit sharing plan", "retirement", "roth", "roth 401k", "rrsp", "sep ira", "simple ira", "sipp", "stock plan", "thrift savings plan", "tfsa", "trust", "ugma", "utma", "variable annuity", "credit card", "paypal", "cd", "checking", "savings", "money market", "prepaid", "auto", "business", "commercial", "construction", "consumer", "home equity", "loan", "mortgage", "overdraft", "line of credit", "student", "cash management", "keogh", "mutual fund", "recurring", "rewards", "safe deposit", "sarsep", "payroll", "null", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """AccountSubtype - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): See the [Account type schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full listing of account types and corresponding subtypes.., must be one of ["401a", "401k", "403B", "457b", "529", "brokerage", "cash isa", "crypto exchange", "education savings account", "ebt", "fixed annuity", "gic", "health reimbursement arrangement", "hsa", "isa", "ira", "lif", "life insurance", "lira", "lrif", "lrsp", "non-custodial wallet", "non-taxable brokerage account", "other", "other insurance", "other annuity", "prif", "rdsp", "resp", "rlif", "rrif", "pension", "profit sharing plan", "retirement", "roth", "roth 401k", "rrsp", "sep ira", "simple ira", "sipp", "stock plan", "thrift savings plan", "tfsa", "trust", "ugma", "utma", "variable annuity", "credit card", "paypal", "cd", "checking", "savings", "money market", "prepaid", "auto", "business", "commercial", "construction", "consumer", "home equity", "loan", "mortgage", "overdraft", "line of credit", "student", "cash management", "keogh", "mutual fund", "recurring", "rewards", "safe deposit", "sarsep", "payroll", "null", ]  # noqa: E501

        Keyword Args:
            value (str): See the [Account type schema](https://plaid.com/docs/api/accounts/#account-type-schema) for a full listing of account types and corresponding subtypes.., must be one of ["401a", "401k", "403B", "457b", "529", "brokerage", "cash isa", "crypto exchange", "education savings account", "ebt", "fixed annuity", "gic", "health reimbursement arrangement", "hsa", "isa", "ira", "lif", "life insurance", "lira", "lrif", "lrsp", "non-custodial wallet", "non-taxable brokerage account", "other", "other insurance", "other annuity", "prif", "rdsp", "resp", "rlif", "rrif", "pension", "profit sharing plan", "retirement", "roth", "roth 401k", "rrsp", "sep ira", "simple ira", "sipp", "stock plan", "thrift savings plan", "tfsa", "trust", "ugma", "utma", "variable annuity", "credit card", "paypal", "cd", "checking", "savings", "money market", "prepaid", "auto", "business", "commercial", "construction", "consumer", "home equity", "loan", "mortgage", "overdraft", "line of credit", "student", "cash management", "keogh", "mutual fund", "recurring", "rewards", "safe deposit", "sarsep", "payroll", "null", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
