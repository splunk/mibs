#
# PySNMP MIB module DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:45 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ObjectIdentity, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("DLINKSW-NETWORK-PROTOCOL-PORT-PROTECT-MIB", dNetworkProtocolPortProtectTCPState=dNetworkProtocolPortProtectTCPState, dNetworkProtocolPortProtectCtrl=dNetworkProtocolPortProtectCtrl, dNetworkProtocolPortProtectObjects=dNetworkProtocolPortProtectObjects, PYSNMP_MODULE_ID=dlinkSwNetworkProtocolPortProtectMIB, dNetworkProtocolPortProtectUDPState=dNetworkProtocolPortProtectUDPState, dlinkSwNetworkProtocolPortProtectMIB=dlinkSwNetworkProtocolPortProtectMIB)
