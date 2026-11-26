#
# PySNMP MIB module DLINKSW-WEB-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-WEB-COMMON-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:27 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Counter64, TimeTicks, ModuleIdentity, iso, Integer32, IpAddress, NotificationType, Counter32, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ModuleIdentity", "iso", "Integer32", "IpAddress", "NotificationType", "Counter32", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
dlinkSwWebCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 162))
dlinkSwWebCommonMIB.setRevisions(('2013-10-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setRevisionsDescriptions(('This is the first version of the MIB file.',))
if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setLastUpdated('201310280000Z')
if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setContactInfo('        D-Link Corporation\n\n                Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                        Taipei City 114, Taiwan, R.O.C\n                Tel:     +886-2-66000123\n                E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwWebCommonMIB.setDescription('The MIB module\tfor configuring Web common feature.\n\t\tThis MIB module contains HTTP and HTTPS configuration.')
dWebCommonMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 0))
dWebMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1))
dWebCommonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2))
dHttpServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1))
dSslServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2))
dHttpServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpServerStatus.setStatus('current')
if mibBuilder.loadTexts: dHttpServerStatus.setDescription('This object indicates the HTTP server feature is support or not.')
dHttpTcpPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(80)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpTcpPort.setStatus('current')
if mibBuilder.loadTexts: dHttpTcpPort.setDescription('This object is Used to configure the TCP port number for HTTP server.\n\t\t\tThe well-known TCP port for the HTTP server is 80.')
dHttpIdleTimeoutVal = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(60, 36000)).clone(180)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dHttpIdleTimeoutVal.setStatus('current')
if mibBuilder.loadTexts: dHttpIdleTimeoutVal.setDescription('This object is Used to set idle timeout of a http server connection in seconds.')
dSslServicePolicyName = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSslServicePolicyName.setStatus('current')
if mibBuilder.loadTexts: dSslServicePolicyName.setDescription('Indicates the name of the policy for SSL application.\n\t\t\tThis node is volatile; that is, it is lost if the SNMP \n            agent is rebooted.')
dSslServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 162, 1, 2, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dSslServerStatus.setStatus('current')
if mibBuilder.loadTexts: dSslServerStatus.setDescription('This object indicates the SSL feature is support or not.')
dWebCommonMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 1))
dWebCommonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2))
dWebMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 1, 1)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dHttpServerGroups"), ("DLINKSW-WEB-COMMON-MIB", "dSslServerGroups"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dWebMIBCompliance = dWebMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: dWebMIBCompliance.setDescription('The compliance statement for entities which implement the \n\t        DLINKSW-WEB-COMMON-MIB.\n\t        ')
dHttpServerGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2, 1)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dHttpServerStatus"), ("DLINKSW-WEB-COMMON-MIB", "dHttpTcpPort"), ("DLINKSW-WEB-COMMON-MIB", "dHttpIdleTimeoutVal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dHttpServerGroups = dHttpServerGroups.setStatus('current')
if mibBuilder.loadTexts: dHttpServerGroups.setDescription('Objects for globally configuring HTTP server feature.\n\t        ')
dSslServerGroups = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 162, 2, 2, 2)).setObjects(("DLINKSW-WEB-COMMON-MIB", "dSslServicePolicyName"), ("DLINKSW-WEB-COMMON-MIB", "dSslServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dSslServerGroups = dSslServerGroups.setStatus('current')
if mibBuilder.loadTexts: dSslServerGroups.setDescription('Objects for globally configuring SSL server feature.\n\t        ')
mibBuilder.exportSymbols("DLINKSW-WEB-COMMON-MIB", dHttpIdleTimeoutVal=dHttpIdleTimeoutVal, dWebCommonMIBNotifications=dWebCommonMIBNotifications, dSslServerGroups=dSslServerGroups, dWebMIBObjects=dWebMIBObjects, dSslServerObjects=dSslServerObjects, dWebCommonGroups=dWebCommonGroups, dHttpServerObjects=dHttpServerObjects, dHttpServerGroups=dHttpServerGroups, dSslServicePolicyName=dSslServicePolicyName, dWebMIBCompliance=dWebMIBCompliance, dHttpServerStatus=dHttpServerStatus, dWebCommonMIBConformance=dWebCommonMIBConformance, dWebCommonMIBCompliances=dWebCommonMIBCompliances, PYSNMP_MODULE_ID=dlinkSwWebCommonMIB, dHttpTcpPort=dHttpTcpPort, dlinkSwWebCommonMIB=dlinkSwWebCommonMIB, dSslServerStatus=dSslServerStatus)
