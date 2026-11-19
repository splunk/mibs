#
# PySNMP MIB module WLSX-TUNNELEDNODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arubaos/WLSX-TUNNELEDNODE-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:55 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
wlsxEnterpriseMibModules, = mibBuilder.importSymbols("ARUBA-MIB", "wlsxEnterpriseMibModules")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, Counter64, snmpModules, Counter32, IpAddress, Gauge32, MibIdentifier, ObjectIdentity, TimeTicks, ModuleIdentity, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "Counter64", "snmpModules", "Counter32", "IpAddress", "Gauge32", "MibIdentifier", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Bits", "Unsigned32")
TextualConvention, PhysAddress, RowStatus, TestAndIncr, TimeInterval, StorageType, MacAddress, TDomain, TruthValue, DisplayString, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "RowStatus", "TestAndIncr", "TimeInterval", "StorageType", "MacAddress", "TDomain", "TruthValue", "DisplayString", "TAddress")
wlsxTunneledNodeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17))
wlsxTunneledNodeMIB.setRevisions(('2020-08-14 17:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setRevisionsDescriptions(('The initial revision.',))
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setLastUpdated('202008141745Z')
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setOrganization('Aruba, a Hewlett Packard Enterprise company')
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setContactInfo('Postal:    3333 Scott Blvd,\n                        Santa Clara, CA 95054\n            E-mail:     aruba-ext-eng-reg@hpe.com\n            Phone:      408 227 4500\n            Fax:        408 752 0626')
if mibBuilder.loadTexts: wlsxTunneledNodeMIB.setDescription('This MIB module defines MIB objects which provide\n            information about the Controller Transport Service (Cts) in the \n\t\t\tAruba controller.')
wlsxTunneledNodeOpGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1))
wlsxTunneledNodeRequestTable = MibTable((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1), )
if mibBuilder.loadTexts: wlsxTunneledNodeRequestTable.setStatus('current')
if mibBuilder.loadTexts: wlsxTunneledNodeRequestTable.setDescription('\n\t\t')
wlsxTunneledNodeRequestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1), ).setIndexNames((0, "WLSX-TUNNELEDNODE-MIB", "wlsxTunneledNodeMAC"))
if mibBuilder.loadTexts: wlsxTunneledNodeRequestEntry.setStatus('current')
if mibBuilder.loadTexts: wlsxTunneledNodeRequestEntry.setDescription('')
wlsxTunneledNodeMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: wlsxTunneledNodeMAC.setStatus('current')
if mibBuilder.loadTexts: wlsxTunneledNodeMAC.setDescription(' \n            MAC address of the Tunneled Node\n            ')
wlsxTunneledNodeIp = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTunneledNodeIp.setStatus('current')
if mibBuilder.loadTexts: wlsxTunneledNodeIp.setDescription('\n            IP address of the Tunneled Node\n\t\t\t')
wlsxNumTunnels = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxNumTunnels.setStatus('current')
if mibBuilder.loadTexts: wlsxNumTunnels.setDescription('\n\t\t\t\tNumber of tunnels originating from Tunneled Node\n\t\t\t')
wlsxTunneledNodeType = MibTableColumn((1, 3, 6, 1, 4, 1, 14823, 2, 2, 1, 17, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("others", 1), ("corvina", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlsxTunneledNodeType.setStatus('current')
if mibBuilder.loadTexts: wlsxTunneledNodeType.setDescription('\n                Device type of the tunnel\n            ')
mibBuilder.exportSymbols("WLSX-TUNNELEDNODE-MIB", wlsxNumTunnels=wlsxNumTunnels, wlsxTunneledNodeRequestEntry=wlsxTunneledNodeRequestEntry, PYSNMP_MODULE_ID=wlsxTunneledNodeMIB, wlsxTunneledNodeType=wlsxTunneledNodeType, wlsxTunneledNodeOpGroup=wlsxTunneledNodeOpGroup, wlsxTunneledNodeMAC=wlsxTunneledNodeMAC, wlsxTunneledNodeMIB=wlsxTunneledNodeMIB, wlsxTunneledNodeIp=wlsxTunneledNodeIp, wlsxTunneledNodeRequestTable=wlsxTunneledNodeRequestTable)
