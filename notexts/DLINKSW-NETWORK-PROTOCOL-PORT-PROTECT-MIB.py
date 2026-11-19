#
# PySNMP MIB module DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:46 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, TimeTicks, ModuleIdentity, NotificationType, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "TimeTicks", "ModuleIdentity", "NotificationType", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "IpAddress")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
dlinkSwNetworkProtocolPortProtectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 194))
dlinkSwNetworkProtocolPortProtectMIB.setRevisions(('2017-11-27 00:00',))
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setLastUpdated('201711270000Z')
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setOrganization('D-Link Corp.')
dNetworkProtocolPortProtectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 194, 1))
dNetworkProtocolPortProtectCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1))
dNetworkProtocolPortProtectTCPState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dNetworkProtocolPortProtectTCPState.setStatus('current')
dNetworkProtocolPortProtectUDPState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dNetworkProtocolPortProtectUDPState.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB", dNetworkProtocolPortProtectObjects=dNetworkProtocolPortProtectObjects, dNetworkProtocolPortProtectUDPState=dNetworkProtocolPortProtectUDPState, dNetworkProtocolPortProtectTCPState=dNetworkProtocolPortProtectTCPState, dNetworkProtocolPortProtectCtrl=dNetworkProtocolPortProtectCtrl, PYSNMP_MODULE_ID=dlinkSwNetworkProtocolPortProtectMIB, dlinkSwNetworkProtocolPortProtectMIB=dlinkSwNetworkProtocolPortProtectMIB)
