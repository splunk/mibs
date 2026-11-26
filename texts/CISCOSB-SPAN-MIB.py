#
# PySNMP MIB module CISCOSB-SPAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-SPAN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rndNotifications, switch001 = mibBuilder.importSymbols("CISCOSB-MIB", "rndNotifications", "switch001")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
class SpanDestinationPortType(TextualConvention, Integer32):
    description = 'SPAN destination mode type:\n                    1 - monitor-only\n                    2 - network.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("monitor-only", 1), ("network", 2))

class SpanSourceType(TextualConvention, Integer32):
    description = 'SPAN source type:\n                    1 - port\n                    2 - VLAN\n                    3 - flow\n                    4 - remote VLAN.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("port", 1), ("vlan", 2), ("flow", 3), ("remote-vlan", 4))

class SpanSourceDirection(TextualConvention, Integer32):
    description = 'SPAN source direction:\n                    1 - rx\n                    2 - tx\n                    3 - both.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rx", 1), ("tx", 2), ("both", 3))

class SpanDestinationReflectorType(TextualConvention, Integer32):
    description = 'RSPAN reflector port type:\n                    1 - SPAN\n                    2 - RSPAN - start\n                    3 - RSPAN - final.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("span", 1), ("rspan-start", 2), ("rspan-final", 3))

rlSpan = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219))
rlSpan.setRevisions(('2015-03-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSpan.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlSpan.setLastUpdated('201503250000Z')
if mibBuilder.loadTexts: rlSpan.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: rlSpan.setContactInfo('Postal: 170 West Tasman Drive\n\tSan Jose , CA 95134-1706\n\tUSA\n\n\t\n\tWebsite:  Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rlSpan.setDescription('This private MIB module for SPAN (Switched Port Analyzer).')
rlSpanMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpanMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlSpanMibVersion.setDescription("MIB's version, the current version is 1.")
rlSpanDestinationTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2), )
if mibBuilder.loadTexts: rlSpanDestinationTable.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationTable.setDescription('The table holds information for SPAN destination per session id.')
rlSpanDestinationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1), ).setIndexNames((0, "CISCOSB-SPAN-MIB", "rlSpanDestinationSessionId"))
if mibBuilder.loadTexts: rlSpanDestinationEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationEntry.setDescription('Entry in the rlSpanDestinationTable.')
rlSpanDestinationSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanDestinationSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationSessionId.setDescription('SPAN session ID. This variable is the key for SPAN destination table.\n         Uniquely identifies the SPAN destination.')
rlSpanDestinationIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationIfIndex.setDescription('Interface Index. This variable identifies the destination ifIndex')
rlSpanDestinationIsReflector = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 3), SpanDestinationReflectorType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationIsReflector.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationIsReflector.setDescription('This variable indicates whether the current session is SPAN or RSPAN \n         start or final session.')
rlSpanDestinationPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 4), SpanDestinationPortType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationPortType.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationPortType.setDescription('This variable indicates whether the destination port acts as network\n         port or analyzer only port.')
rlSpanDestinationRemoteVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 5), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRemoteVlanId.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationRemoteVlanId.setDescription('This variable indicated the remote vlan id for RSPAN case.')
rlSpanDestinationRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanDestinationRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlSpanDestinationRowStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
rlSpanSourceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3), )
if mibBuilder.loadTexts: rlSpanSourceTable.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceTable.setDescription('The table holds information for SPAN Source ports per session id.')
rlSpanSourceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1), ).setIndexNames((0, "CISCOSB-SPAN-MIB", "rlSpanSourceSessionId"), (0, "CISCOSB-SPAN-MIB", "rlSpanSourceType"), (0, "CISCOSB-SPAN-MIB", "rlSpanSourceIndex"))
if mibBuilder.loadTexts: rlSpanSourceEntry.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceEntry.setDescription('Entry in the rlSpanSourceTable.')
rlSpanSourceSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: rlSpanSourceSessionId.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceSessionId.setDescription('SPAN session ID. This variable is the key for SPAN source table.\n         Identifies the SPAN source.')
rlSpanSourceType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 2), SpanSourceType())
if mibBuilder.loadTexts: rlSpanSourceType.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceType.setDescription('This variable indicates the SPAN source type.')
rlSpanSourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 3), Integer32())
if mibBuilder.loadTexts: rlSpanSourceIndex.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceIndex.setDescription('This variable indicates the ifIndex of the SPAN source port\n         or the flow Id of the class map (for flow span source type).')
rlSpanSourceDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 4), SpanSourceDirection()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceDirection.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceDirection.setDescription('This variable indicates the source direction for monitoring.')
rlSpanSourceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 219, 3, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpanSourceRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlSpanSourceRowStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
mibBuilder.exportSymbols("CISCOSB-SPAN-MIB", rlSpanDestinationSessionId=rlSpanDestinationSessionId, rlSpanSourceDirection=rlSpanSourceDirection, rlSpanSourceRowStatus=rlSpanSourceRowStatus, rlSpanMibVersion=rlSpanMibVersion, SpanDestinationPortType=SpanDestinationPortType, rlSpanSourceType=rlSpanSourceType, rlSpanSourceEntry=rlSpanSourceEntry, rlSpanDestinationPortType=rlSpanDestinationPortType, rlSpanDestinationIfIndex=rlSpanDestinationIfIndex, rlSpanSourceIndex=rlSpanSourceIndex, rlSpanDestinationIsReflector=rlSpanDestinationIsReflector, SpanSourceType=SpanSourceType, rlSpan=rlSpan, rlSpanDestinationRowStatus=rlSpanDestinationRowStatus, PYSNMP_MODULE_ID=rlSpan, rlSpanDestinationTable=rlSpanDestinationTable, SpanSourceDirection=SpanSourceDirection, rlSpanSourceTable=rlSpanSourceTable, SpanDestinationReflectorType=SpanDestinationReflectorType, rlSpanDestinationRemoteVlanId=rlSpanDestinationRemoteVlanId, rlSpanSourceSessionId=rlSpanSourceSessionId, rlSpanDestinationEntry=rlSpanDestinationEntry)
