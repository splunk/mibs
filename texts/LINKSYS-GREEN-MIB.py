#
# PySNMP MIB module LINKSYS-GREEN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/linksys/LINKSYS-GREEN-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:38:11 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("LINKSYS-MIB", "rnd")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, NotificationType, Unsigned32, iso, Integer32, TimeTicks, Counter32, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "NotificationType", "Unsigned32", "iso", "Integer32", "TimeTicks", "Counter32", "IpAddress", "ObjectIdentity")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlGreenEth = ModuleIdentity((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134))
rlGreenEth.setRevisions(('2008-08-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlGreenEth.setRevisionsDescriptions(('Add Green Ethernet Energy Detect and Short Reach support per port and per system rlGreenEthernet',))
if mibBuilder.loadTexts: rlGreenEth.setLastUpdated('200808150000Z')
if mibBuilder.loadTexts: rlGreenEth.setOrganization('Linksys LLC.')
if mibBuilder.loadTexts: rlGreenEth.setContactInfo('www.linksys.com/business/support')
if mibBuilder.loadTexts: rlGreenEth.setDescription('The private MIB module definition for Green Ethernet Energy Detect feature.')
rlGreenEthEnergyDetectEnable = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthEnergyDetectEnable.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthEnergyDetectEnable.setDescription('This scalar defines Green Ethernet Enrgy-Detect Globaly')
rlGreenEthShortReachEnable = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachEnable.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthShortReachEnable.setDescription('This scalar defines Green Ethernet Short-Reach Globaly')
rlGreenEthCurrentEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 3), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentEnergyConsumption.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthCurrentEnergyConsumption.setDescription('This scalar define Green Ethernet all modes current Energy consumption per system in mWatt\n         in order to calculate current energy consumption in percent proportional to Consumption without Green Ethernet feature\n         please use the following formula:\n         (rlGreenEthCurrentEnergyConsumption/rlGreenEthCurrentMaxEnergyConsumption)*100')
rlGreenEthCurrentMaxEnergyConsumption = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 4), Unsigned32()).setUnits('mWatt').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCurrentMaxEnergyConsumption.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthCurrentMaxEnergyConsumption.setDescription('This scalar define Green Ethernet current maximum consumption Energy consumption per system in mWatt,\n         as it was without Green Ethernet feature.')
rlGreenEthCumulativePowerSaveMeter = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 5), Unsigned32()).setUnits('Watt*Hour').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeter.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeter.setDescription('This scalar define Green Ethernet cumulative power save per system in Watt*Hour')
rlGreenEthShortReachThreshold = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 70))).setUnits('meter').setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthShortReachThreshold.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthShortReachThreshold.setDescription('The usage threshold expressed in meter for\n                determinate the cable length for Short-Reach')
rlGreenEthCumulativePowerSaveMeterReset = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeterReset.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthCumulativePowerSaveMeterReset.setDescription("The rlGreenEthCumulativePowerSaveMeterReset indicates that rlGreenEthCumulativePowerSaveMeter\n            should be set to ziro.\n\n            This object behaviors as write-only than\n            reading this object will always return 'false'.")
class RlGreenSavingType(TextualConvention, Integer32):
    description = 'Green saving types:\n         energyDetect(1)  uses energy detect\n         shortReach(2)  uses Short Reach'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("energyDetect", 1), ("shortReach", 2))

class NonOperReasonType(TextualConvention, Integer32):
    description = 'Reason why Green Ethernet is not activated saving on a port\n         NP(1)                  Port is not present - Applicable in ED & SR\n         LT(2)                  Link Type is not supported(fiber, auto media setect) - Applicable in ED & SR\n         LU(3)                  Port link is up - Applicable only in ED\n         LS(4)                  Link speed is not supported (100M,10M,10G) - Applicable only in SR\n         LL(5)                  Link length received from VCT test exceed threshold - Applicable only in SR\n         ER(6)                  Errors detected on line and port revered back to Long Reach(only in enhanced mode) - Applicable only in SR\n         LD(7)                  Port link is Down - Applicable only in SR\n         unknown(8)             In case that green Active or disable on port'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("np", 1), ("lt", 2), ("lu", 3), ("ls", 4), ("ll", 5), ("er", 6), ("ld", 7), ("unknown", 8))

rlGreenEthPortTable = MibTable((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8), )
if mibBuilder.loadTexts: rlGreenEthPortTable.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortTable.setDescription('A table of green state of ports')
rlGreenEthPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "LINKSYS-GREEN-MIB", "rlGreenEthPortSavingTypeValue"))
if mibBuilder.loadTexts: rlGreenEthPortEntry.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortEntry.setDescription('An entry of green state of port')
rlGreenEthPortSavingTypeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1, 1), RlGreenSavingType())
if mibBuilder.loadTexts: rlGreenEthPortSavingTypeValue.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortSavingTypeValue.setDescription('Green saving types')
rlGreenEthPortAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthPortAdminState.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortAdminState.setDescription('Active\\non Active')
rlGreenEthPortOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortOperState.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortOperState.setDescription('Active\\non Active')
rlGreenEthPortNonOperReason = MibTableColumn((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 8, 1, 4), NonOperReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGreenEthPortNonOperReason.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthPortNonOperReason.setDescription('Reason why saving mode is not activated')
rlGreenEthForceShortReachIfIndexList = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 9), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthForceShortReachIfIndexList.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthForceShortReachIfIndexList.setDescription('The ports that forced enable the Green Ethernet Short Reach configuration\n          not considering VCT results.')
rlGreenEthMaskLedStatus = MibScalar((1, 3, 6, 1, 4, 1, 3955, 1000, 201, 134, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGreenEthMaskLedStatus.setStatus('current')
if mibBuilder.loadTexts: rlGreenEthMaskLedStatus.setDescription('Mask all ports led  according to the configuration.')
mibBuilder.exportSymbols("LINKSYS-GREEN-MIB", rlGreenEthCurrentEnergyConsumption=rlGreenEthCurrentEnergyConsumption, rlGreenEthPortEntry=rlGreenEthPortEntry, rlGreenEthMaskLedStatus=rlGreenEthMaskLedStatus, rlGreenEthShortReachThreshold=rlGreenEthShortReachThreshold, rlGreenEthShortReachEnable=rlGreenEthShortReachEnable, rlGreenEthPortSavingTypeValue=rlGreenEthPortSavingTypeValue, rlGreenEthPortAdminState=rlGreenEthPortAdminState, rlGreenEth=rlGreenEth, rlGreenEthPortTable=rlGreenEthPortTable, rlGreenEthForceShortReachIfIndexList=rlGreenEthForceShortReachIfIndexList, rlGreenEthEnergyDetectEnable=rlGreenEthEnergyDetectEnable, rlGreenEthCurrentMaxEnergyConsumption=rlGreenEthCurrentMaxEnergyConsumption, rlGreenEthCumulativePowerSaveMeter=rlGreenEthCumulativePowerSaveMeter, rlGreenEthPortOperState=rlGreenEthPortOperState, PYSNMP_MODULE_ID=rlGreenEth, rlGreenEthPortNonOperReason=rlGreenEthPortNonOperReason, NonOperReasonType=NonOperReasonType, RlGreenSavingType=RlGreenSavingType, rlGreenEthCumulativePowerSaveMeterReset=rlGreenEthCumulativePowerSaveMeterReset)
