#
# PySNMP MIB module ACOS-VRRPA-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-VRRPA-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:04:33 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, ObjectIdentity, Bits, IpAddress, MibIdentifier, Counter64, NotificationType, Integer32, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "ObjectIdentity", "Bits", "IpAddress", "MibIdentifier", "Counter64", "NotificationType", "Integer32", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
vrrpACommonModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6))
if mibBuilder.loadTexts: vrrpACommonModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: vrrpACommonModule.setOrganization('A10 Networks, Inc.')
if mibBuilder.loadTexts: vrrpACommonModule.setContactInfo('Address: A10 Networks, Inc.\n\t\t\t\t\t\t\t  2300 Orchard Parkway\n\t\t\t\t\t\t\t  San Jose, CA 95131\n\t\t\t\t\t\t Phone:   +1-888-822-7210 (USA/Canada)\n\t\t\t\t\t\t          +1-408-325-8676 (International)\n\t\t\t\t\t\t E-mail:  support@A10Networks.com')
if mibBuilder.loadTexts: vrrpACommonModule.setDescription('vrrpACommonModule OID for ACOS')
common = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1))
commonStatsTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1, 1), )
if mibBuilder.loadTexts: commonStatsTable.setStatus('current')
if mibBuilder.loadTexts: commonStatsTable.setDescription("HA VRRP-A Global Commands from object 'vrrp-a.common'")
commonStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1, 1, 1), ).setIndexNames((0, "ACOS-VRRPA-COMMON-MIB", "commonStatsSlotId"))
if mibBuilder.loadTexts: commonStatsEntry.setStatus('current')
if mibBuilder.loadTexts: commonStatsEntry.setDescription('The commonStats stats entry')
commonStatsSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonStatsSlotId.setStatus('current')
if mibBuilder.loadTexts: commonStatsSlotId.setDescription('')
commonStatsVrrpCommonDummy = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 6, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: commonStatsVrrpCommonDummy.setStatus('current')
if mibBuilder.loadTexts: commonStatsVrrpCommonDummy.setDescription('vrrp_common_dummy')
mibBuilder.exportSymbols("ACOS-VRRPA-COMMON-MIB", commonStatsSlotId=commonStatsSlotId, PYSNMP_MODULE_ID=vrrpACommonModule, common=common, commonStatsTable=commonStatsTable, vrrpACommonModule=vrrpACommonModule, commonStatsVrrpCommonDummy=commonStatsVrrpCommonDummy, commonStatsEntry=commonStatsEntry)
