#
# PySNMP MIB module AT-HHM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-HHM-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:05:06 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
DisplayStringUnsized, = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, NotificationType, Bits, Integer32, MibIdentifier, iso, TimeTicks, IpAddress, Unsigned32, Counter64, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Bits", "Integer32", "MibIdentifier", "iso", "TimeTicks", "IpAddress", "Unsigned32", "Counter64", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atHwHealthMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24))
atHwHealthMon.setRevisions(('2013-06-28 00:00',))
if mibBuilder.loadTexts: atHwHealthMon.setLastUpdated('201306280000Z')
if mibBuilder.loadTexts: atHwHealthMon.setOrganization('Allied Telesis, Inc')
atHhmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 0))
atHhmLogNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 0, 1)).setObjects(("AT-HHM-MIB", "atHhmLogMessage"))
if mibBuilder.loadTexts: atHhmLogNotify.setStatus('current')
atHhmNotificationVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 1))
atHhmLogMessage = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 24, 1, 1), DisplayStringUnsized().subtype(subtypeSpec=ValueSizeConstraint(0, 200))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: atHhmLogMessage.setStatus('current')
mibBuilder.exportSymbols("AT-HHM-MIB", PYSNMP_MODULE_ID=atHwHealthMon, atHwHealthMon=atHwHealthMon, atHhmLogNotify=atHhmLogNotify, atHhmLogMessage=atHhmLogMessage, atHhmNotificationVariables=atHhmNotificationVariables, atHhmNotifications=atHhmNotifications)
