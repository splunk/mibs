#
# PySNMP MIB module DLINKSW-GENMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-GENMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:45 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, TimeTicks, Gauge32, iso, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, ObjectIdentity, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "TimeTicks", "Gauge32", "iso", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("DLINKSW-GENMGMT-MIB", dGenMgmtMIBObjects=dGenMgmtMIBObjects, dGenMgmtNotifyInfos=dGenMgmtNotifyInfos, dGenMgmtMIBConformance=dGenMgmtMIBConformance, dlinkSwGenMgmtMIB=dlinkSwGenMgmtMIB, dGenMgmtNotifyInfoUserName=dGenMgmtNotifyInfoUserName, dGenMgmtMIBNotifications=dGenMgmtMIBNotifications, PYSNMP_MODULE_ID=dlinkSwGenMgmtMIB, dGenMgmtLoginFail=dGenMgmtLoginFail, dGenMgmtNotifyInfoLoginType=dGenMgmtNotifyInfoLoginType)
