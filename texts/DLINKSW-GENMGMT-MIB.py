#
# PySNMP MIB module DLINKSW-GENMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-GENMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:27 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, ModuleIdentity, iso, Integer32, IpAddress, NotificationType, Counter32, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "ModuleIdentity", "iso", "Integer32", "IpAddress", "NotificationType", "Counter32", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dlinkSwGenMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 165))
if mibBuilder.loadTexts: dlinkSwGenMgmtMIB.setLastUpdated('201309130000Z')
if mibBuilder.loadTexts: dlinkSwGenMgmtMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: dlinkSwGenMgmtMIB.setContactInfo('        D-Link Corporation\n\n             Postal: No. 289, Sinhu 3rd Rd., Neihu District,\n                     Taipei City 114, Taiwan, R.O.C\n             Tel:     +886-2-66000123\n             E-mail: tsd@dlink.com.tw\n            ')
if mibBuilder.loadTexts: dlinkSwGenMgmtMIB.setDescription('This is the first version of the MIB file.')
dGenMgmtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 165, 0))
dGenMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 165, 1))
dGenMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 165, 2))
dGenMgmtLoginFail = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 165, 0, 1)).setObjects(("DLINKSW-GENMGMT-MIB", "dGenMgmtNotifyInfoLoginType"), ("DLINKSW-GENMGMT-MIB", "dGenMgmtNotifyInfoUserName"))
if mibBuilder.loadTexts: dGenMgmtLoginFail.setStatus('current')
if mibBuilder.loadTexts: dGenMgmtLoginFail.setDescription('Generated when the user login failed to the switch.')
dGenMgmtNotifyInfos = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1))
dGenMgmtNotifyInfoLoginType = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("console", 1), ("telnet", 2), ("ssh", 3), ("web", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dGenMgmtNotifyInfoLoginType.setStatus('current')
if mibBuilder.loadTexts: dGenMgmtNotifyInfoLoginType.setDescription('The type is the user login method type.')
dGenMgmtNotifyInfoUserName = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dGenMgmtNotifyInfoUserName.setStatus('current')
if mibBuilder.loadTexts: dGenMgmtNotifyInfoUserName.setDescription('This object is the name of the user that login to the switch.')
mibBuilder.exportSymbols("DLINKSW-GENMGMT-MIB", dGenMgmtMIBObjects=dGenMgmtMIBObjects, PYSNMP_MODULE_ID=dlinkSwGenMgmtMIB, dlinkSwGenMgmtMIB=dlinkSwGenMgmtMIB, dGenMgmtNotifyInfoUserName=dGenMgmtNotifyInfoUserName, dGenMgmtNotifyInfos=dGenMgmtNotifyInfos, dGenMgmtMIBNotifications=dGenMgmtMIBNotifications, dGenMgmtMIBConformance=dGenMgmtMIBConformance, dGenMgmtLoginFail=dGenMgmtLoginFail, dGenMgmtNotifyInfoLoginType=dGenMgmtNotifyInfoLoginType)
