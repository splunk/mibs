#
# PySNMP MIB module CISCO-FLOW-MONITOR-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-FLOW-MONITOR-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoFlowMonitorTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 688))
ciscoFlowMonitorTcMIB.setRevisions(('2008-12-09 00:00',))
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setLastUpdated('200812090000Z')
if mibBuilder.loadTexts: ciscoFlowMonitorTcMIB.setOrganization('Cisco Systems, Inc.')
class FlowMonitorIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowPointType(TextualConvention, Integer32):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("none", 3), ("interface", 4), ("dot1qVlan", 5))

class FlowPointIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FlowPointInterface(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    displayHint = '4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class FlowPointDot1qVlan(TextualConvention, OctetString):
    reference = "K. McCloghrie and F. Kastenholz, 'The Interfaces Group MIB', RFC-2863, June 2000."
    status = 'current'
    displayHint = '4d,2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class FlowMetrics(TextualConvention, Bits):
    reference = "H. Schulzrinne, S. Casner, R. Fredrick, and V. Jacobson, 'RTP: A Transport Protocol for Real-Time Applications', RFC-3550, July 2003. J. Welch and J. Clark, 'A Proposed Media Delivery Index (MDI)', RFC-4445, APril 2006."
    status = 'current'
    namedValues = NamedValues(("mdi", 0), ("rtp", 1), ("ipCbr", 2))

class FlowCfgRateType(TextualConvention, Integer32):
    reference = "J. Welch and J. Clark, 'A Proposed Media Delivery Index (MDI)', RFC-4445, APril 2006."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("auto", 1), ("ipPktRate", 2), ("ipBitRate", 3), ("mediaRate", 4))

class FlowBitRateUnits(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("bps", 1), ("kbps", 2), ("mbps", 3), ("gbps", 4))

class FlowMetricScale(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class FlowMetricPrecision(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(-8, -1), ValueRangeConstraint(1, 9), )
class FlowMetricValue(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class FlowMonitorConditions(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FlowMonitorConditionsProfile(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowMonitorConditionsProfileOrZero(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class FlowMonitorConditionIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 2039)

class FlowMonitorAlarmGroupIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FlowSetIdentifier(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

mibBuilder.exportSymbols("CISCO-FLOW-MONITOR-TC-MIB", FlowSetIdentifier=FlowSetIdentifier, FlowMonitorIdentifier=FlowMonitorIdentifier, FlowMetricValue=FlowMetricValue, FlowPointIdentifier=FlowPointIdentifier, ciscoFlowMonitorTcMIB=ciscoFlowMonitorTcMIB, FlowMonitorConditionIdentifier=FlowMonitorConditionIdentifier, FlowMonitorConditions=FlowMonitorConditions, FlowMonitorConditionsProfile=FlowMonitorConditionsProfile, FlowBitRateUnits=FlowBitRateUnits, FlowMonitorAlarmGroupIdentifier=FlowMonitorAlarmGroupIdentifier, FlowCfgRateType=FlowCfgRateType, FlowMonitorConditionsProfileOrZero=FlowMonitorConditionsProfileOrZero, FlowMetrics=FlowMetrics, FlowIdentifier=FlowIdentifier, FlowPointInterface=FlowPointInterface, FlowMetricPrecision=FlowMetricPrecision, FlowPointDot1qVlan=FlowPointDot1qVlan, FlowPointType=FlowPointType, FlowMetricScale=FlowMetricScale, PYSNMP_MODULE_ID=ciscoFlowMonitorTcMIB)
