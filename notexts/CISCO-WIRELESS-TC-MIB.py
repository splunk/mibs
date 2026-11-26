#
# PySNMP MIB module CISCO-WIRELESS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-WIRELESS-TC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoWirelessTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 137))
ciscoWirelessTextualConventions.setRevisions(('2000-04-03 00:00',))
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setLastUpdated('200004030000Z')
if mibBuilder.loadTexts: ciscoWirelessTextualConventions.setOrganization('Cisco Systems, Inc.')
class CwrRFZeroIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2)

class CwrCwErrorFreeSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwErroredSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwSeverelyErroredSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwConsecutiveSevErrSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwDegradedSecond(TextualConvention, Gauge32):
    status = 'current'

class CwrCwDegradedMinute(TextualConvention, Gauge32):
    status = 'current'

class CwrCollectionAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("actionStop", 1), ("actionStart", 2), ("actionClear", 3), ("actionRestart", 4))

class CwrCollectionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("statusIdle", 1), ("statusInProgress", 2), ("statusStopped", 3), ("statusCaptured", 4))

class CwrdBm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-80, 33)

class CwrdB(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 16)

class CwrThreshLimitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("upChange", 1), ("downChange", 2), ("highThresh", 3), ("lowThresh", 4), ("upLimit", 5), ("lowLimit", 6))

class CwrRadioSignalAttribute(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("rsaIN", 1), ("rsaINR", 2), ("rsaConstellationVariance", 3), ("rsaTimingOffset", 4), ("rsaReceivedPower", 5), ("rsaGainSettingsIF", 6), ("rsaGainSettingsRF", 7), ("rsaFreqOffset", 8), ("rsaTotalGain", 9), ("rsaSyncStatus", 10))

class CwrOscState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oscillatorOk", 1), ("osccillatorBad", 2))

class P2mpRadioSignalAttribute(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 0), ("rsaSinrMainAnt", 1), ("rsaSinrDiversityAnt", 2), ("rsaSinrRatio", 3), ("rsaTimingOffset", 4), ("rsaRxPowerMainAnt", 5), ("rsaRxPowerDiversityAnt", 6), ("rsaChDelaySpreadMainAnt", 7), ("rsaChDelaySpreadDiversityAnt", 8), ("rsaHeAmbientNoise", 9), ("rsaSuRxPowerDeltaMainAnt", 10), ("rsaSuRxPowerDeltaDiversityAnt", 11), ("rsaSuTotalTxPower", 12))

class CwrRfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("main", 0), ("diversity", 1))

class CwrFixedPointScale(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("yocto", 1), ("zepto", 2), ("atto", 3), ("femto", 4), ("pico", 5), ("nano", 6), ("micro", 7), ("milli", 8), ("units", 9), ("kilo", 10), ("mega", 11), ("giga", 12), ("tera", 13), ("exa", 14), ("peta", 15), ("zetta", 16), ("yotta", 17))

class CwrFixedPointPrecision(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 9)

class CwrFixedPointValue(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-2147483648, 2147483647)

class P2mpSnapshotAttribute(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 1)
    fixedLength = 1

class CwrPercentageValue(TextualConvention, Gauge32):
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 10000000)

class CwrUpdateTime(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CwrRfFreqRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 60000000)

class WirelessGauge64(TextualConvention, Counter64):
    status = 'current'

mibBuilder.exportSymbols("CISCO-WIRELESS-TC-MIB", CwrFixedPointPrecision=CwrFixedPointPrecision, CwrCwDegradedSecond=CwrCwDegradedSecond, CwrCwConsecutiveSevErrSecond=CwrCwConsecutiveSevErrSecond, CwrRfFreqRange=CwrRfFreqRange, CwrRfType=CwrRfType, CwrCwErroredSecond=CwrCwErroredSecond, P2mpSnapshotAttribute=P2mpSnapshotAttribute, CwrdBm=CwrdBm, CwrCollectionAction=CwrCollectionAction, CwrCwSeverelyErroredSecond=CwrCwSeverelyErroredSecond, CwrCollectionStatus=CwrCollectionStatus, CwrCwDegradedMinute=CwrCwDegradedMinute, CwrCwErrorFreeSecond=CwrCwErrorFreeSecond, CwrPercentageValue=CwrPercentageValue, CwrOscState=CwrOscState, CwrdB=CwrdB, CwrUpdateTime=CwrUpdateTime, CwrThreshLimitType=CwrThreshLimitType, PYSNMP_MODULE_ID=ciscoWirelessTextualConventions, ciscoWirelessTextualConventions=ciscoWirelessTextualConventions, WirelessGauge64=WirelessGauge64, CwrFixedPointScale=CwrFixedPointScale, CwrFixedPointValue=CwrFixedPointValue, CwrRadioSignalAttribute=CwrRadioSignalAttribute, P2mpRadioSignalAttribute=P2mpRadioSignalAttribute, CwrRFZeroIndex=CwrRFZeroIndex)
