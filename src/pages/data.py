from dataclasses import dataclass

from src.pages.main_site.data import MainSitePageData


@dataclass
class IngData:
    main_site_page: MainSitePageData
