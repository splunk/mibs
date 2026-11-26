#
# PySNMP MIB module DLINKSW-MAC-AUTH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-MAC-AUTH-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
dnaSessionClientMacAddress, dnaSessionAuthVlan = mibBuilder.importSymbols("DLINKSW-NETWORK-ACCESS-MIB", "dnaSessionClientMacAddress", "dnaSessionAuthVlan")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, TimeTicks, NotificationType, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "TimeTicks", "NotificationType", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
dlinkSwMacAuthMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 153))
dlinkSwMacAuthMIB.setRevisions(('2013-08-02 00:00',))
if mibBuilder.loadTexts: dlinkSwMacAuthMIB.setLastUpdated('201308020000Z')
if mibBuilder.loadTexts: dlinkSwMacAuthMIB.setOrganization('D-Link Corp.')
dMacAuthNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 153, 0))
dMacAuthMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 153, 1))
dMacAuthMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 153, 2))
dMacAuthGlobalCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 153, 1, 1))
dMacAuthNotifEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 153, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dMacAuthNotifEnabled.setStatus('current')
dMacAuthEnabled = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 153, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dMacAuthEnabled.setStatus('current')
dMacAuthPWD = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 153, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dMacAuthPWD.setStatus('current')
dMacAuthUserName = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 153, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dMacAuthUserName.setStatus('current')
dMacAuthIfTable = MibTable((1, 3, 6, 1, 4, 1, 171, 14, 153, 1, 2), )
if mibBuilder.loadTexts: dMacAuthIfTable.setStatus('current')
dMacAuthIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 14, 153, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dMacAuthIfEntry.setStatus('current')
dMacAuthIfEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 14, 153, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dMacAuthIfEnabled.setStatus('current')
dMacAuthLoggedSuccess = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 153, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-NETWORK-ACCESS-MIB", "dnaSessionClientMacAddress"), ("DLINKSW-NETWORK-ACCESS-MIB", "dnaSessionAuthVlan"))
if mibBuilder.loadTexts: dMacAuthLoggedSuccess.setStatus('current')
dMacAuthLoggedFail = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 153, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-NETWORK-ACCESS-MIB", "dnaSessionClientMacAddress"), ("DLINKSW-NETWORK-ACCESS-MIB", "dnaSessionAuthVlan"))
if mibBuilder.loadTexts: dMacAuthLoggedFail.setStatus('current')
dMacAuthLoggedAgesOut = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 153, 0, 3)).setObjects(("IF-MIB", "ifIndex"), ("DLINKSW-NETWORK-ACCESS-MIB", "dnaSessionClientMacAddress"), ("DLINKSW-NETWORK-ACCESS-MIB", "dnaSessionAuthVlan"))
if mibBuilder.loadTexts: dMacAuthLoggedAgesOut.setStatus('current')
dMacAuthMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 153, 2, 1))
dMacAuthMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 153, 2, 2))
dMacAuthMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 14, 153, 2, 1, 1)).setObjects(("DLINKSW-MAC-AUTH-MIB", "dMacAuthGlobalCfgGroup"), ("DLINKSW-MAC-AUTH-MIB", "dMacAuthIfCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dMacAuthMIBCompliance = dMacAuthMIBCompliance.setStatus('current')
dMacAuthGlobalCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 153, 2, 2, 1)).setObjects(("DLINKSW-MAC-AUTH-MIB", "dMacAuthEnabled"), ("DLINKSW-MAC-AUTH-MIB", "dMacAuthPWD"), ("DLINKSW-MAC-AUTH-MIB", "dMacAuthUserName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dMacAuthGlobalCfgGroup = dMacAuthGlobalCfgGroup.setStatus('current')
dMacAuthIfCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 153, 2, 2, 2)).setObjects(("DLINKSW-MAC-AUTH-MIB", "dMacAuthIfEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dMacAuthIfCfgGroup = dMacAuthIfCfgGroup.setStatus('current')
dMacAuthNotifyCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 14, 153, 2, 2, 3)).setObjects(("DLINKSW-MAC-AUTH-MIB", "dMacAuthNotifEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dMacAuthNotifyCfgGroup = dMacAuthNotifyCfgGroup.setStatus('current')
dMacAuthNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 171, 14, 153, 2, 2, 4)).setObjects(("DLINKSW-MAC-AUTH-MIB", "dMacAuthLoggedSuccess"), ("DLINKSW-MAC-AUTH-MIB", "dMacAuthLoggedFail"), ("DLINKSW-MAC-AUTH-MIB", "dMacAuthLoggedAgesOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dMacAuthNotificationGroup = dMacAuthNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-MAC-AUTH-MIB", PYSNMP_MODULE_ID=dlinkSwMacAuthMIB, dMacAuthIfEntry=dMacAuthIfEntry, dMacAuthLoggedAgesOut=dMacAuthLoggedAgesOut, dMacAuthEnabled=dMacAuthEnabled, dlinkSwMacAuthMIB=dlinkSwMacAuthMIB, dMacAuthGlobalCtrl=dMacAuthGlobalCtrl, dMacAuthNotifEnabled=dMacAuthNotifEnabled, dMacAuthNotificationGroup=dMacAuthNotificationGroup, dMacAuthIfTable=dMacAuthIfTable, dMacAuthIfCfgGroup=dMacAuthIfCfgGroup, dMacAuthMIBObjects=dMacAuthMIBObjects, dMacAuthMIBConformance=dMacAuthMIBConformance, dMacAuthNotifyCfgGroup=dMacAuthNotifyCfgGroup, dMacAuthGlobalCfgGroup=dMacAuthGlobalCfgGroup, dMacAuthIfEnabled=dMacAuthIfEnabled, dMacAuthPWD=dMacAuthPWD, dMacAuthMIBCompliance=dMacAuthMIBCompliance, dMacAuthMIBCompliances=dMacAuthMIBCompliances, dMacAuthNotifications=dMacAuthNotifications, dMacAuthLoggedFail=dMacAuthLoggedFail, dMacAuthLoggedSuccess=dMacAuthLoggedSuccess, dMacAuthUserName=dMacAuthUserName, dMacAuthMIBGroups=dMacAuthMIBGroups)
