# -*- coding: utf-8 -*-
from openprocurement.auctions.core.adapters import (
    AuctionConfigurator,
    AuctionManagerAdapter,
    Manager,
)
from openprocurement.auctions.core.utils import (
    apply_patch,
    save_auction,
)
from openprocurement.auctions.rubble.models import (
    RubbleOther,
    RubbleFinancial
)
from openprocurement.auctions.core.plugins.awarding.v2_1.adapters import (
    AwardingV2_1ConfiguratorMixin
)


class RubbleRelatedProcessesManager(Manager):
    def create(self, request):
        self.context.relatedProcesses.append(request.validated['relatedProcess'])
        return save_auction(request)

    def update(self, request):
        return apply_patch(request, src=request.context.serialize())

    def delete(self, request):
        self.context.relatedProcesses.remove(request.validated['relatedProcess'])
        self.context.modified = False
        return save_auction(request)


class AuctionRubbleOtherConfigurator(AuctionConfigurator,
                                     AwardingV2_1ConfiguratorMixin):
    name = 'Auction Rubble Configurator'
    model = RubbleOther


class AuctionRubbleFinancialConfigurator(AuctionConfigurator,
                                         AwardingV2_1ConfiguratorMixin):
    name = 'Auction Rubble Configurator'
    model = RubbleFinancial


class AuctionRubbleOtherManagerAdapter(AuctionManagerAdapter):

    def __init__(self, *args, **kwargs):
        super(AuctionRubbleOtherManagerAdapter, self).__init__(*args, **kwargs)
        context = args[0]
        self.related_processes_manager = RubbleRelatedProcessesManager(parent=context, parent_name='context')

    def create_auction(self, request):
        pass

    def change_auction(self, request):
        pass


class AuctionRubbleFinancialManagerAdapter(AuctionManagerAdapter):

    def __init__(self, *args, **kwargs):
        super(AuctionRubbleFinancialManagerAdapter, self).__init__(*args, **kwargs)
        context = args[0]
        self.related_processes_manager = RubbleRelatedProcessesManager(parent=context, parent_name='context')

    def create_auction(self, request):
        pass

    def change_auction(self, request):
        pass
