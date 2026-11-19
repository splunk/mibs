#
# PySNMP MIB module ACOS-VRRPA-MAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-VRRPA-MAC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:03 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, Integer32, Gauge32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Integer32", "Gauge32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
vrrpAMacModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11))
if mibBuilder.loadTexts: vrrpAMacModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: vrrpAMacModule.setOrganization('A10 Networks, Inc.')
mac = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11, 1))
macOperVridMacListTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11, 1, 2), )
if mibBuilder.loadTexts: macOperVridMacListTable.setStatus('current')
macOperVridMacListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11, 1, 2, 1), ).setIndexNames((0, "ACOS-VRRPA-MAC-MIB", "macOperVridMacListSlotId"), (0, "ACOS-VRRPA-MAC-MIB", "macOperVridMacListVridMacListListId"))
if mibBuilder.loadTexts: macOperVridMacListEntry.setStatus('current')
macOperVridMacListSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macOperVridMacListSlotId.setStatus('current')
macOperVridMacListVridMacListListId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macOperVridMacListVridMacListListId.setStatus('current')
macOperVridMacListVrid = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macOperVridMacListVrid.setStatus('current')
macOperVridMacListMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macOperVridMacListMacAddress.setStatus('current')
macOperVridMacListMacWithSynCookie = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 11, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macOperVridMacListMacWithSynCookie.setStatus('current')
mibBuilder.exportSymbols("ACOS-VRRPA-MAC-MIB", macOperVridMacListVrid=macOperVridMacListVrid, macOperVridMacListMacWithSynCookie=macOperVridMacListMacWithSynCookie, mac=mac, macOperVridMacListMacAddress=macOperVridMacListMacAddress, vrrpAMacModule=vrrpAMacModule, macOperVridMacListVridMacListListId=macOperVridMacListVridMacListListId, macOperVridMacListEntry=macOperVridMacListEntry, macOperVridMacListTable=macOperVridMacListTable, macOperVridMacListSlotId=macOperVridMacListSlotId, PYSNMP_MODULE_ID=vrrpAMacModule)
