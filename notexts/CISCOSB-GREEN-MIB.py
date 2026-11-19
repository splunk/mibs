#
# PySNMP MIB module CISCOSB-GREEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-GREEN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:34:43 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, Integer32, Bits, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Integer32", "Bits", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "Counter32")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlGreenEth = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134))
rlGreenEth.setRevisions(('2008-08-15 00:00',))
if mibBuilder.loadTexts: rlGreenEth.setLastUpdated('200808150000Z')
if mibBuilder.loadTexts: rlGreenEth.setOrganization('Cisco Systems, Inc.')
rlGreenEthEnergyDetectEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthEnergyDetectEnable.setStatus('current')
rlGreenEthShortReachEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachEnable.setStatus('current')
rlGreenEthCurrentEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 3), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentEnergyConsumption.setStatus('current')
rlGreenEthCurrentMaxEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 4), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentMaxEnergyConsumption.setStatus('current')
rlGreenEthCumulativePowerSaveMeter = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 5), Unsigned32()).setUnits('Watt*Hour').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeter.setStatus('current')
rlGreenEthShortReachThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 70))).setUnits('meter').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachThreshold.setStatus('current')
rlGreenEthCumulativePowerSaveMeterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeterReset.setStatus('current')
class RlGreenSavingType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("energyDetect", 1), ("shortReach", 2))

class NonOperReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("np", 1), ("lt", 2), ("lu", 3), ("ls", 4), ("ll", 5), ("er", 6), ("ld", 7), ("unknown", 8))

class CableLengthRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("lengthUnknown", 0), ("lengthLessThan50M", 1), ("length50MTo80M", 2), ("length80MTo110M", 3), ("length110MTo140M", 4), ("lengthMoreThan140M", 5))

rlGreenEthPortTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8), )
if mibBuilder.loadTexts: rlGreenEthPortTable.setStatus('current')
rlGreenEthPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCOSB-GREEN-MIB", "rlGreenEthPortSavingTypeValue"))
if mibBuilder.loadTexts: rlGreenEthPortEntry.setStatus('current')
rlGreenEthPortSavingTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 1), RlGreenSavingType())
if mibBuilder.loadTexts: rlGreenEthPortSavingTypeValue.setStatus('current')
rlGreenEthPortAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthPortAdminState.setStatus('current')
rlGreenEthPortOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortOperState.setStatus('current')
rlGreenEthPortNonOperReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 4), NonOperReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortNonOperReason.setStatus('current')
rlGreenEthPortCableLength = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 8, 1, 5), CableLengthRange()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortCableLength.setStatus('current')
rlGreenEthForceShortReachIfIndexList = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 9), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthForceShortReachIfIndexList.setStatus('current')
rlGreenEthMaskLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 134, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthMaskLedStatus.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-GREEN-MIB", rlGreenEthCumulativePowerSaveMeter=rlGreenEthCumulativePowerSaveMeter, rlGreenEthEnergyDetectEnable=rlGreenEthEnergyDetectEnable, rlGreenEthPortAdminState=rlGreenEthPortAdminState, rlGreenEthShortReachEnable=rlGreenEthShortReachEnable, rlGreenEthPortNonOperReason=rlGreenEthPortNonOperReason, rlGreenEthPortSavingTypeValue=rlGreenEthPortSavingTypeValue, rlGreenEthPortOperState=rlGreenEthPortOperState, RlGreenSavingType=RlGreenSavingType, rlGreenEthShortReachThreshold=rlGreenEthShortReachThreshold, NonOperReasonType=NonOperReasonType, rlGreenEthForceShortReachIfIndexList=rlGreenEthForceShortReachIfIndexList, rlGreenEthCumulativePowerSaveMeterReset=rlGreenEthCumulativePowerSaveMeterReset, rlGreenEthCurrentMaxEnergyConsumption=rlGreenEthCurrentMaxEnergyConsumption, PYSNMP_MODULE_ID=rlGreenEth, rlGreenEthCurrentEnergyConsumption=rlGreenEthCurrentEnergyConsumption, CableLengthRange=CableLengthRange, rlGreenEthPortCableLength=rlGreenEthPortCableLength, rlGreenEthMaskLedStatus=rlGreenEthMaskLedStatus, rlGreenEthPortTable=rlGreenEthPortTable, rlGreenEthPortEntry=rlGreenEthPortEntry, rlGreenEth=rlGreenEth)
