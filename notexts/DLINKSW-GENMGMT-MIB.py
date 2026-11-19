#
# PySNMP MIB module DLINKSW-GENMGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dlink/DLINKSW-GENMGMT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:46 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
dlinkIndustrialCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkIndustrialCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, TimeTicks, ModuleIdentity, NotificationType, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "TimeTicks", "ModuleIdentity", "NotificationType", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter32", "Counter64", "IpAddress")
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
mibBuilder.exportSymbols("DLINKSW-GENMGMT-MIB", PYSNMP_MODULE_ID=dlinkSwGenMgmtMIB, dGenMgmtNotifyInfoLoginType=dGenMgmtNotifyInfoLoginType, dGenMgmtMIBConformance=dGenMgmtMIBConformance, dGenMgmtNotifyInfoUserName=dGenMgmtNotifyInfoUserName, dGenMgmtMIBNotifications=dGenMgmtMIBNotifications, dGenMgmtNotifyInfos=dGenMgmtNotifyInfos, dGenMgmtLoginFail=dGenMgmtLoginFail, dlinkSwGenMgmtMIB=dlinkSwGenMgmtMIB, dGenMgmtMIBObjects=dGenMgmtMIBObjects)
