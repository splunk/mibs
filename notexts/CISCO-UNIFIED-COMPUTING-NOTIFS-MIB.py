#
# PySNMP MIB module CISCO-UNIFIED-COMPUTING-NOTIFS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-UNIFIED-COMPUTING-NOTIFS-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cucsFaultLastModificationTime, cucsFaultSeverity, cucsFaultOccur, cucsFaultDescription, cucsFaultCode, cucsFaultCreationTime, cucsFaultAffectedObjectId, cucsFaultProbableCause, cucsFaultId, cucsFaultAffectedObjectDn, cucsFaultIndex, cucsFaultType = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime", "cucsFaultSeverity", "cucsFaultOccur", "cucsFaultDescription", "cucsFaultCode", "cucsFaultCreationTime", "cucsFaultAffectedObjectId", "cucsFaultProbableCause", "cucsFaultId", "cucsFaultAffectedObjectDn", "cucsFaultIndex", "cucsFaultType")
ciscoUnifiedComputingMIB, ciscoUnifiedComputingMIBObjects = mibBuilder.importSymbols("CISCO-UNIFIED-COMPUTING-MIB", "ciscoUnifiedComputingMIB", "ciscoUnifiedComputingMIBObjects")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoUnifiedComputingMIBNotifs = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 719, 0))
ciscoUnifiedComputingMIBNotifs.setRevisions(('2010-01-29 00:00',))
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBNotifs.setLastUpdated('201001290000Z')
if mibBuilder.loadTexts: ciscoUnifiedComputingMIBNotifs.setOrganization('Cisco')
cucsFaultActiveNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 1)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
if mibBuilder.loadTexts: cucsFaultActiveNotif.setStatus('current')
cucsFaultClearNotif = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 719, 0, 2)).setObjects(("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultIndex"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultDescription"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectId"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultAffectedObjectDn"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCreationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultLastModificationTime"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultCode"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultType"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultProbableCause"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultSeverity"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultOccur"), ("CISCO-UNIFIED-COMPUTING-FAULT-MIB", "cucsFaultId"))
if mibBuilder.loadTexts: cucsFaultClearNotif.setStatus('current')
mibBuilder.exportSymbols("CISCO-UNIFIED-COMPUTING-NOTIFS-MIB", cucsFaultClearNotif=cucsFaultClearNotif, ciscoUnifiedComputingMIBNotifs=ciscoUnifiedComputingMIBNotifs, PYSNMP_MODULE_ID=ciscoUnifiedComputingMIBNotifs, cucsFaultActiveNotif=cucsFaultActiveNotif)
