#
# PySNMP MIB module LINKSYS-BONJOUR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-BONJOUR-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:37:19 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Bits, Counter32, Gauge32, IpAddress, Unsigned32, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Bits", "Counter32", "Gauge32", "IpAddress", "Unsigned32", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rlBonjour = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114))
rlBonjour.setRevisions(('2009-04-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlBonjour.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlBonjour.setLastUpdated('200909210000Z')
if mibBuilder.loadTexts: rlBonjour.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlBonjour.setContactInfo('linksys.com')
if mibBuilder.loadTexts: rlBonjour.setDescription('The private MIB module definition for Bonjour protocol.')
rlBonjourPublish = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourPublish.setStatus('current')
if mibBuilder.loadTexts: rlBonjourPublish.setDescription('Enables or disables Bonjour publishing.')
class RlBonjourServiceState(TextualConvention, Integer32):
    description = 'Bonjour service status - (per IP interface).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("rlBonjourNotPublished", 0), ("rlBonjourInactive", 1), ("rlBonjourRegistering", 2), ("rlBonjourRunning", 3))

class RlBonjourOperationState(TextualConvention, Integer32):
    description = 'Bonjour service an L2 interface operation state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class RlBonjourOperationReason(TextualConvention, Integer32):
    description = 'Bonjour service an L2 interface operation state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("notExclude", 0), ("include", 1), ("notInclude", 2), ("exclude", 3), ("bonjourDisabled", 4), ("serviceDisabled", 5), ("noIPaddress", 6), ("l2InterfaceDown", 7), ("notPresent", 8), ("unknown", 9))

rlBonjourStatusTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2), )
if mibBuilder.loadTexts: rlBonjourStatusTable.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusTable.setDescription('The table listing the service bonjour status per service and IP interface.\n        In order to keep the table sorted according to the customary lexicographical\n        order of the rlBonjourStatusServiceName strings, rlBonjourStatusServiceName\n        will be padded with blanks. Bonjour will truncate the padded blanks when advertising this service name.\n\n        Using this MIB user can monitor actual state of a service on an IP interface')
rlBonjourStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1), ).setIndexNames((0, "LINKSYS-BONJOUR-MIB", "rlBonjourStatusServiceName"), (0, "LINKSYS-BONJOUR-MIB", "rlBonjourStatusIPInterfaceType"), (0, "LINKSYS-BONJOUR-MIB", "rlBonjourStatusIPInterfaceAddr"))
if mibBuilder.loadTexts: rlBonjourStatusEntry.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusEntry.setDescription(' An entry in the rlBonjourStatusEntry.')
rlBonjourStatusServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlBonjourStatusServiceName.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusServiceName.setDescription('This variable identifies the service name.')
rlBonjourStatusIPInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceType.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceType.setDescription('This variable indicates the type of the IP interface\n       on which the Bonjour service should be published.')
rlBonjourStatusIPInterfaceAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1, 3), InetAddress())
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceAddr.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusIPInterfaceAddr.setDescription('This variable indicates the address of the IP interface\n       on which the Bonjour service should be published.')
rlBonjourStatusState = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 2, 1, 4), RlBonjourServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStatusState.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStatusState.setDescription('This variable identifies the service state on IP interface of the device.')
rlBonjourStateTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3), )
if mibBuilder.loadTexts: rlBonjourStateTable.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateTable.setDescription("The table listing the service bonjour state per service and L2 interface.\n        The services that are displayed here are only those who are supported per project.\n        The L2 interfaces that are displayed  here are either:\n             L2 interfaces with an IP on it\n                    OR\n             L2 interfaces listed in the table below\n        Per each pair (service and L2 interface) table displays:\n            state :\n                UP   - Bonjour published the service on this L2 interface\n                    Not-exclude - the L2 interface has IP address (L2 interface is in UP state)\n                                    AND rlBonjourL2Table is empty\n                                    AND rlBonjourL2Mode is disable\n                    include - the L2 interfaces are listed in the table rlBonjourL2Table\n                                AND rlBonjourL2Mode is enabled\n                Down - Bonjour sent goodbye packets regarding this service on this L2 interface\n                    exclude - the L2 interface is a member of the rlBonjourL2Table\n                              AND rlBonjourL2Mode is disable\n                    Not-Include - rlBonjourL2Table is empty\n                                  AND rlBonjourL2Mode is enable\n                    service disabled - service was removed ue to specific request from L1 manager\n                    No IP address    - the L2 interfaces is listed in the table rlBonjourL2EnableTable\n                                       BUT don't have an IP on it\n                    Not-present      - the L2 interfaces is listed in the table rlBonjourL2EnableTable\n                                       BUT no yet defined (like vlan not created or port in an unconnected salve)\n                    Bonjour disabled - rlBonjourPublish scalar is off\n        Using this MIB user can monitor actual state of a service on an IP interface")
rlBonjourStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1), ).setIndexNames((0, "LINKSYS-BONJOUR-MIB", "rlBonjourStateServiceName"), (0, "LINKSYS-BONJOUR-MIB", "rlBonjourStateL2Interface"))
if mibBuilder.loadTexts: rlBonjourStateEntry.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateEntry.setDescription(' An entry in the rlBonjourStatusEntry.')
rlBonjourStateServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1, 1), DisplayString())
if mibBuilder.loadTexts: rlBonjourStateServiceName.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateServiceName.setDescription('This variable identifies the service name.')
rlBonjourStateL2Interface = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: rlBonjourStateL2Interface.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateL2Interface.setDescription('This variable indicates the L2 interface\n       on which the Bonjour service should be published.')
rlBonjourStateOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1, 3), RlBonjourOperationState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateOperationMode.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateOperationMode.setDescription('This variable indicates wether Bonjour is operational on the pair (service + L2 interface).')
rlBonjourStateOperationReason = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 3, 1, 4), RlBonjourOperationReason()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourStateOperationReason.setStatus('current')
if mibBuilder.loadTexts: rlBonjourStateOperationReason.setDescription('This variable specifies the reason of the previous field: rlBonjourStateOperationMode.')
rlBonjourL2Table = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 4), )
if mibBuilder.loadTexts: rlBonjourL2Table.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2Table.setDescription("The table listing the L2 interfaces on which the user wishes to\n        enable OR disable Bonjour with respect to rlBonjourL2Mode.\n        If rlBonjourL2Mode is set to include AND L2 interface is in this table\n        it does not ensure Bonjour WILL publish services on it.\n        Publication is also dependent on these fundemental conditions:\n            rlBonjourPublish must be on\n            at least one service should be enabled\n            L2 must be present and UP\n            have at least one IP on it\n        If this table is empty AND rlBonjourL2Mode is set to include\n        Bonjour won't operate at all.\n        If rlBonjourL2Mode is set to exclude, and rlBonjourL2Table is empty\n        Bonjour will be published on ALL L2 interfaces answering to the\n        fundemental conditions specified above.\n        If rlBonjourL2Table is NOT empty then Bonjour will operate on\n        ALL L2 interfaces answering to the fundemental conditions specified\n        above BUT NOT members of this list.\n      ")
rlBonjourL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 4, 1), ).setIndexNames((0, "LINKSYS-BONJOUR-MIB", "rlBonjourL2Ifindex"))
if mibBuilder.loadTexts: rlBonjourL2Entry.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2Entry.setDescription(' An entry in the rlBonjourL2Entry.')
rlBonjourL2Ifindex = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rlBonjourL2Ifindex.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2Ifindex.setDescription('This variable identifies the L2 interface.')
rlBonjourL2RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 4, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourL2RowStatus.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2RowStatus.setDescription('This variable identifies the L2 interface status manager.')
rlBonjourL2Mode = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("include", 1), ("exclude", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlBonjourL2Mode.setStatus('current')
if mibBuilder.loadTexts: rlBonjourL2Mode.setDescription('specify whether the L2 interfaces listed in rlBonjourL2Table\n         means include bonjour on these L2 interfaces once they:\n            rlBonjourPublish must be on\n            at least one service should be enabled\n            L2 must be present and UP\n            have at least one IP on it\n         OR  exclude bonjour on these L2 interfaces even if they answer to\n         all the conditions above.')
rlBonjourInstanceName = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourInstanceName.setStatus('current')
if mibBuilder.loadTexts: rlBonjourInstanceName.setDescription('Instance Name is given to Bonjour driver by the project part (L1Manager)\n        When a conflict occurs: found another station with the same instance name.\n        Bonjour driver is required to append _m to the given name\n        while m is an incremental integer, increasing on each conflict')
rlBonjourHostName = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 114, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlBonjourHostName.setStatus('current')
if mibBuilder.loadTexts: rlBonjourHostName.setDescription('Host Name is given to Bonjour driver by the project part (L1Manager)\n        When a conflict occurs: found another station with the same host name.\n        Bonjour driver is required to append _m to the given name\n        while m is an incremental integer, increasing on each conflict')
mibBuilder.exportSymbols("LINKSYS-BONJOUR-MIB", rlBonjourStatusState=rlBonjourStatusState, rlBonjourInstanceName=rlBonjourInstanceName, rlBonjourStateServiceName=rlBonjourStateServiceName, rlBonjourL2Mode=rlBonjourL2Mode, RlBonjourOperationState=RlBonjourOperationState, rlBonjourL2Ifindex=rlBonjourL2Ifindex, PYSNMP_MODULE_ID=rlBonjour, rlBonjourPublish=rlBonjourPublish, rlBonjourStatusIPInterfaceType=rlBonjourStatusIPInterfaceType, RlBonjourServiceState=RlBonjourServiceState, rlBonjourStatusServiceName=rlBonjourStatusServiceName, rlBonjourStateTable=rlBonjourStateTable, rlBonjourL2Entry=rlBonjourL2Entry, rlBonjourStateOperationMode=rlBonjourStateOperationMode, rlBonjourHostName=rlBonjourHostName, RlBonjourOperationReason=RlBonjourOperationReason, rlBonjourL2Table=rlBonjourL2Table, rlBonjourL2RowStatus=rlBonjourL2RowStatus, rlBonjourStatusEntry=rlBonjourStatusEntry, rlBonjourStateL2Interface=rlBonjourStateL2Interface, rlBonjourStatusIPInterfaceAddr=rlBonjourStatusIPInterfaceAddr, rlBonjourStateOperationReason=rlBonjourStateOperationReason, rlBonjour=rlBonjour, rlBonjourStateEntry=rlBonjourStateEntry, rlBonjourStatusTable=rlBonjourStatusTable)
