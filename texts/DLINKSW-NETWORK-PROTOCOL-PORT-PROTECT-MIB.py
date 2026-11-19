#
# PySNMP MIB module DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:48 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, ModuleIdentity, Bits, IpAddress, iso, NotificationType, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Bits", "IpAddress", "iso", "NotificationType", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
dlinkSwNetworkProtocolPortProtectMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 194))
dlinkSwNetworkProtocolPortProtectMIB.setRevisions(('2017-11-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setRevisionsDescriptions((' This is the first version of the MIB file.\n            ',))
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setLastUpdated('201711270000Z')
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setContactInfo('        D-Link Corporation\n\n             Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                     Taipei City 114, Taiwan, R.O.C\n             Tel:     +886-2-66000123\n             E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwNetworkProtocolPortProtectMIB.setDescription('This MIB module defines objects for network protocol port protect.')
dNetworkProtocolPortProtectObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 194, 1))
dNetworkProtocolPortProtectCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1))
dNetworkProtocolPortProtectTCPState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dNetworkProtocolPortProtectTCPState.setStatus('current')
if mibBuilder.loadTexts: dNetworkProtocolPortProtectTCPState.setDescription('When enable it switch will not response for the closed TCP port.')
dNetworkProtocolPortProtectUDPState = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 194, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dNetworkProtocolPortProtectUDPState.setStatus('current')
if mibBuilder.loadTexts: dNetworkProtocolPortProtectUDPState.setDescription('When enable it switch will not response for the closed UDP port.')
mibBuilder.exportSymbols("DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB", dlinkSwNetworkProtocolPortProtectMIB=dlinkSwNetworkProtocolPortProtectMIB, dNetworkProtocolPortProtectCtrl=dNetworkProtocolPortProtectCtrl, dNetworkProtocolPortProtectTCPState=dNetworkProtocolPortProtectTCPState, PYSNMP_MODULE_ID=dlinkSwNetworkProtocolPortProtectMIB, dNetworkProtocolPortProtectObjects=dNetworkProtocolPortProtectObjects, dNetworkProtocolPortProtectUDPState=dNetworkProtocolPortProtectUDPState)
