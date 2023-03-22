"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
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
)


class LinkEventName(ModelSimple):
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
            'BANK_INCOME_INSIGHTS_COMPLETED': "BANK_INCOME_INSIGHTS_COMPLETED",
            'CLOSE_OAUTH': "CLOSE_OAUTH",
            'ERROR': "ERROR",
            'EXIT': "EXIT",
            'FAIL_OAUTH': "FAIL_OAUTH",
            'HANDOFF': "HANDOFF",
            'OPEN': "OPEN",
            'OPEN_MY_PLAID': "OPEN_MY_PLAID",
            'OPEN_OAUTH': "OPEN_OAUTH",
            'SEARCH_INSTITUTION': "SEARCH_INSTITUTION",
            'SELECT_AUTH_TYPE': "SELECT_AUTH_TYPE",
            'SELECT_BRAND': "SELECT_BRAND",
            'SELECT_DEGRADED_INSTITUTION': "SELECT_DEGRADED_INSTITUTION",
            'SELECT_DOWN_INSTITUTION': "SELECT_DOWN_INSTITUTION",
            'SELECT_INSTITUTION': "SELECT_INSTITUTION",
            'SUBMIT_ACCOUNT_NUMBER': "SUBMIT_ACCOUNT_NUMBER",
            'SUBMIT_CREDENTIALS': "SUBMIT_CREDENTIALS",
            'SUBMIT_DOCUMENTS': "SUBMIT_DOCUMENTS",
            'SUBMIT_DOCUMENTS_ERROR': "SUBMIT_DOCUMENTS_ERROR",
            'SUBMIT_DOCUMENTS_SUCCESS': "SUBMIT_DOCUMENTS_SUCCESS",
            'SUBMIT_MFA': "SUBMIT_MFA",
            'SUBMIT_ROUTING_NUMBER': "SUBMIT_ROUTING_NUMBER",
            'TRANSITION_VIEW': "TRANSITION_VIEW",
            'VIEW_DATA_TYPES': "VIEW_DATA_TYPES",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

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
        """LinkEventName - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): A string representing the event that has just occurred in the Link flow.., must be one of ["BANK_INCOME_INSIGHTS_COMPLETED", "CLOSE_OAUTH", "ERROR", "EXIT", "FAIL_OAUTH", "HANDOFF", "OPEN", "OPEN_MY_PLAID", "OPEN_OAUTH", "SEARCH_INSTITUTION", "SELECT_AUTH_TYPE", "SELECT_BRAND", "SELECT_DEGRADED_INSTITUTION", "SELECT_DOWN_INSTITUTION", "SELECT_INSTITUTION", "SUBMIT_ACCOUNT_NUMBER", "SUBMIT_CREDENTIALS", "SUBMIT_DOCUMENTS", "SUBMIT_DOCUMENTS_ERROR", "SUBMIT_DOCUMENTS_SUCCESS", "SUBMIT_MFA", "SUBMIT_ROUTING_NUMBER", "TRANSITION_VIEW", "VIEW_DATA_TYPES", ]  # noqa: E501

        Keyword Args:
            value (str): A string representing the event that has just occurred in the Link flow.., must be one of ["BANK_INCOME_INSIGHTS_COMPLETED", "CLOSE_OAUTH", "ERROR", "EXIT", "FAIL_OAUTH", "HANDOFF", "OPEN", "OPEN_MY_PLAID", "OPEN_OAUTH", "SEARCH_INSTITUTION", "SELECT_AUTH_TYPE", "SELECT_BRAND", "SELECT_DEGRADED_INSTITUTION", "SELECT_DOWN_INSTITUTION", "SELECT_INSTITUTION", "SUBMIT_ACCOUNT_NUMBER", "SUBMIT_CREDENTIALS", "SUBMIT_DOCUMENTS", "SUBMIT_DOCUMENTS_ERROR", "SUBMIT_DOCUMENTS_SUCCESS", "SUBMIT_MFA", "SUBMIT_ROUTING_NUMBER", "TRANSITION_VIEW", "VIEW_DATA_TYPES", ]  # noqa: E501
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
