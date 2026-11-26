#
# PySNMP MIB module DLINKSW-GENMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-GENMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:08:25 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Bits, Counter64, NotificationType, TimeTicks, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Bits", "Counter64", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlinkSwGenMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 14, 165))
if mibBuilder.loadTexts: dlinkSwGenMgmtMIB.setLastUpdated('201309130000Z')
if mibBuilder.loadTexts: dlinkSwGenMgmtMIB.setOrganization('D-Link Corp.')
dGenMgmtMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 165, 0))
dGenMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 165, 1))
dGenMgmtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 165, 2))
dGenMgmtLoginFail = NotificationType((1, 3, 6, 1, 4, 1, 171, 14, 165, 0, 1)).setObjects(("DLINKSW-GENMGMT-MIB", "dGenMgmtNotifyInfoLoginType"), ("DLINKSW-GENMGMT-MIB", "dGenMgmtNotifyInfoUserName"))
if mibBuilder.loadTexts: dGenMgmtLoginFail.setStatus('current')
dGenMgmtNotifyInfos = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1))
dGenMgmtNotifyInfoLoginType = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("console", 1), ("telnet", 2), ("ssh", 3), ("web", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dGenMgmtNotifyInfoLoginType.setStatus('current')
dGenMgmtNotifyInfoUserName = MibScalar((1, 3, 6, 1, 4, 1, 171, 14, 165, 1, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: dGenMgmtNotifyInfoUserName.setStatus('current')
mibBuilder.exportSymbols("DLINKSW-GENMGMT-MIB", dGenMgmtMIBConformance=dGenMgmtMIBConformance, dGenMgmtNotifyInfos=dGenMgmtNotifyInfos, dGenMgmtLoginFail=dGenMgmtLoginFail, dGenMgmtNotifyInfoUserName=dGenMgmtNotifyInfoUserName, dGenMgmtNotifyInfoLoginType=dGenMgmtNotifyInfoLoginType, dGenMgmtMIBObjects=dGenMgmtMIBObjects, dGenMgmtMIBNotifications=dGenMgmtMIBNotifications, PYSNMP_MODULE_ID=dlinkSwGenMgmtMIB, dlinkSwGenMgmtMIB=dlinkSwGenMgmtMIB)
