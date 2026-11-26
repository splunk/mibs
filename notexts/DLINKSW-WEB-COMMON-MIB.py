#
# PySNMP MIB module DLINKSW-WEB-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-WEB-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
dlinkSwWebCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 162))
dlinkSwWebCommonMIB.setRevisions(('2013-10-28 00:00',))
if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setLastUpdated('201310280000Z')
if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setOrganization('D-Link Corp.')
dWebCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 0))
dWebMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1))
dWebCommonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2))
dHttpServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1))
dSslServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2))
dHttpServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpServerStatus.setStatus('current')
dHttpTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpTcpPort.setStatus('current')
dHttpIdleTimeoutVal = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 36000)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpIdleTimeoutVal.setStatus('current')
dSslServicePolicyName = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSslServicePolicyName.setStatus('current')
dSslServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSslServerStatus.setStatus('current')
dWebCommonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 1))
dWebCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2))
dWebMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 1, 1)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dHttpServerGroups"), ("DLINKSW-WEB-COMMON-MIB", "dSslServerGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dWebMIBCompliance = dWebMIBCompliance.setStatus('current')
dHttpServerGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2, 1)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dHttpServerStatus"), ("DLINKSW-WEB-COMMON-MIB", "dHttpTcpPort"), ("DLINKSW-WEB-COMMON-MIB", "dHttpIdleTimeoutVal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dHttpServerGroups = dHttpServerGroups.setStatus('current')
dSslServerGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2, 2)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dSslServicePolicyName"), ("DLINKSW-WEB-COMMON-MIB", "dSslServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSslServerGroups = dSslServerGroups.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-WEB-COMMON-MIB", dHttpServerGroups=dHttpServerGroups, dHttpIdleTimeoutVal=dHttpIdleTimeoutVal, dHttpTcpPort=dHttpTcpPort, dWebMIBObjects=dWebMIBObjects, dWebMIBCompliance=dWebMIBCompliance, dSslServerGroups=dSslServerGroups, dWebCommonMIBNotifications=dWebCommonMIBNotifications, dSslServicePolicyName=dSslServicePolicyName, PYSNMP_MODULE_ID=dlinkSwWebCommonMIB, dHttpServerStatus=dHttpServerStatus, dWebCommonMIBConformance=dWebCommonMIBConformance, dSslServerStatus=dSslServerStatus, dSslServerObjects=dSslServerObjects, dWebCommonMIBCompliances=dWebCommonMIBCompliances, dlinkSwWebCommonMIB=dlinkSwWebCommonMIB, dWebCommonGroups=dWebCommonGroups, dHttpServerObjects=dHttpServerObjects)
