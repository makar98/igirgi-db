from .resources.customer_full_data.api import CustomerFullDataApi, CustomersFullDataApi
from .resources.customer.api import CustomerApi, CustomersApi
from .resources.field.api import FieldApi, FieldsApi
from .resources.pad.api import PadApi, PadsApi
from .resources.well.api import WellApi, WellsApi
from .resources.wellbore.api import WellboreApi, WellboresApi
from .resources.suite.api import SuiteApi, SuitesApi
from .resources.layer.api import LayerApi, LayersApi

from .resources.service_company.api import ServiceCompaniesApi, ServiceCompanyApi
from .resources.tool.api import ToolApi, ToolsApi
from .resources.gis_curve.api import GisCurveApi, GisCurvesApi
from .resources.gis_curve_category.api import GisCurveCategoryApi, GisCurveCategoriesApi
from .resources.gis_rename_curve.api import GisRenameCurveApi, GisRenameCurvesApi
from .resources.quality_sheet.api import QualitySheetApi, QualitySheetsApi

#GTI
from .resources.gti.parameter.api import GtiParameterApi, GtiParametersApi
from .resources.gti.format.api import GtiFormatApi, GtiFormatsApi

from .resources.gti.service_company.api import GtiServiceCompanyApi, GtiServiceCompaniesApi

from .resources.gti.station_type.api import GtiStationTypeApi, GtiStationTypesApi

from .resources.gti.chromatograph_type.api import GtiChromatographTypeApi, GtiChromatographTypesApi

from .resources.gti.degasser_type.api import GtiDegasserApi, GtiDegassersApi

from .resources.logger.api import LoggerApi, LoggersApi


def initialize_routes(api):
    api.add_resource(CustomerFullDataApi, '/api/customer_full_data/<customer_id>')
    api.add_resource(CustomersFullDataApi, '/api/customer_full_data', '/api/customers_full_data')

    api.add_resource(CustomerApi, '/api/customer/<customer_id>')
    api.add_resource(CustomersApi, '/api/customer', '/api/customers')

    api.add_resource(FieldApi, '/api/field/<field_id>')
    api.add_resource(FieldsApi, '/api/field', '/api/fields')

    api.add_resource(PadApi, '/api/pad/<pad_id>')
    api.add_resource(PadsApi, '/api/pad', '/api/pads')

    api.add_resource(WellApi, '/api/well/<well_id>')
    api.add_resource(WellsApi, '/api/well', '/api/wells')

    api.add_resource(WellboreApi, '/api/wellbore/<wellbore_id>')
    api.add_resource(WellboresApi, '/api/wellbore', '/api/wellbores')

    api.add_resource(SuiteApi, '/api/suite/<suite_id>')
    api.add_resource(SuitesApi, '/api/suite', '/api/suites')

    api.add_resource(LayerApi, '/api/layer/<layer_id>')
    api.add_resource(LayersApi, '/api/layer', '/api/layers')

    # GIS
    api.add_resource(ServiceCompanyApi, '/api/service_company/<service_company_id>')
    api.add_resource(ServiceCompaniesApi, '/api/service_company', '/api/service_companies')

    api.add_resource(GisCurveApi, '/api/gis_curve/<gis_curve_id>')
    api.add_resource(GisCurvesApi, '/api/gis_curve', '/api/gis_curves')

    api.add_resource(GisCurveCategoryApi, '/api/gis_category/<gis_category_id>')
    api.add_resource(GisCurveCategoriesApi, '/api/gis_category', '/api/gis_categories')

    api.add_resource(GisRenameCurveApi, '/api/gis_rename_curve/<gis_rename_curve_id>')
    api.add_resource(GisRenameCurvesApi, '/api/gis_rename_curve', '/api/gis_rename_curves')

    #api.add_resource(QualitySheetApi, '/api/quality_sheet/<quality_sheet_id>')
    #api.add_resource(QualitySheetsApi, '/api/quality_sheet', '/api/quality_sheets')

    #GTI
    api.add_resource(GtiParameterApi, '/api/gti/parameter/<parameter_id>')
    api.add_resource(GtiParametersApi, '/api/gti/parameter', '/api/gti/parameters')

    api.add_resource(GtiFormatApi, '/api/gti/format/<gti_format_id>')
    api.add_resource(GtiFormatsApi, '/api/gti/format', '/api/gti/formats')

    api.add_resource(GtiServiceCompanyApi, '/api/gti/company/<company_id>')
    api.add_resource(GtiServiceCompaniesApi, '/api/gti/company', '/api/gti/companies')

    api.add_resource(GtiStationTypeApi, '/api/gti/station_type/<station_type_id>')
    api.add_resource(GtiStationTypesApi, '/api/gti/station_type', '/api/gti/station_types')

    api.add_resource(GtiChromatographTypeApi, '/api/gti/chromatograph_type/<chromatograph_type_id>')
    api.add_resource(GtiChromatographTypesApi, '/api/gti/chromatograph_type', '/api/gti/chromatograph_types')

    api.add_resource(GtiDegasserApi, '/api/gti/degasser_type/<degasser_type_id>')
    api.add_resource(GtiDegassersApi, '/api/gti/degasser_type', '/api/gti/degasser_types')

    api.add_resource(LoggerApi, '/api/logger/<log_id>')
    api.add_resource(LoggersApi, '/api/logger', '/api/loggers')

