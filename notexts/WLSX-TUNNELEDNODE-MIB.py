#
# PySNMP MIB module WLSX-TUNNELEDNODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/WLSX-TUNNELEDNODE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:53 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Unsigned32, Bits, Gauge32, TimeTicks, ModuleIdentity, snmpModules, MibIdentifier, Integer32, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Unsigned32", "Bits", "Gauge32", "TimeTicks", "ModuleIdentity", "snmpModules", "MibIdentifier", "Integer32", "ObjectIdentity", "NotificationType")
DisplayString, TimeInterval, TDomain, MacAddress, RowStatus, StorageType, TestAndIncr, PhysAddress, TextualConvention, TruthValue, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeInterval", "TDomain", "MacAddress", "RowStatus", "StorageType", "TestAndIncr", "PhysAddress", "TextualConvention", "TruthValue", "TAddress")
wlsxTunneledNodeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17))
wlsxTunneledNodeMIB.setRevisions(('2020-08-14 17:45',))
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setLastUpdated('202008141745Z')
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setOrganization('Aruba, a Hewlett Packard Enterprise company')
wlsxTunneledNodeOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1))
wlsxTunneledNodeRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1), )
if mibBuilder.loadTexts: wlsxTunneledNodeRequestTable.setStatus('current')
wlsxTunneledNodeRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1), ).setIndexNames((0, "WLSX-TUNNELEDNODE-MIB", "wlsxTunneledNodeMAC"))
if mibBuilder.loadTexts: wlsxTunneledNodeRequestEntry.setStatus('current')
wlsxTunneledNodeMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: wlsxTunneledNodeMAC.setStatus('current')
wlsxTunneledNodeIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTunneledNodeIp.setStatus('current')
wlsxNumTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumTunnels.setStatus('current')
wlsxTunneledNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("others", 1), ("corvina", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTunneledNodeType.setStatus('current')
mibBuilder.exportSymbols("WLSX-TUNNELEDNODE-MIB", wlsxTunneledNodeMAC=wlsxTunneledNodeMAC, wlsxTunneledNodeType=wlsxTunneledNodeType, wlsxTunneledNodeRequestTable=wlsxTunneledNodeRequestTable, PYSNMP_MODULE_ID=wlsxTunneledNodeMIB, wlsxNumTunnels=wlsxNumTunnels, wlsxTunneledNodeRequestEntry=wlsxTunneledNodeRequestEntry, wlsxTunneledNodeOpGroup=wlsxTunneledNodeOpGroup, wlsxTunneledNodeMIB=wlsxTunneledNodeMIB, wlsxTunneledNodeIp=wlsxTunneledNodeIp)
