#
# PySNMP MIB module CISCO-IMAGE-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IMAGE-TC
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoImageTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 455))
ciscoImageTc.setRevisions(('2005-01-12 00:00',))
if mibBuilder.loadTexts: ciscoImageTc.setLastUpdated('200501120000Z')
if mibBuilder.loadTexts: ciscoImageTc.setOrganization('Cisco Systems, Inc.')
class CeImageInstallableStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("active", 1), ("pendingInstall", 2), ("pendingRemoval", 3), ("installPendingReload", 4), ("removedPendingReload", 5), ("installPendingReloadPendingRemoval", 6), ("removedPendingReloadPendingInstall", 7), ("pruned", 8), ("inactive", 9))

class CeImageInstallableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("base", 1), ("patch", 2), ("script", 3), ("package", 4), ("compositePackage", 5), ("softwareMaintenanceUpgrade", 6))

mibBuilder.exportSymbols("CISCO-IMAGE-TC", CeImageInstallableType=CeImageInstallableType, PYSNMP_MODULE_ID=ciscoImageTc, ciscoImageTc=ciscoImageTc, CeImageInstallableStatus=CeImageInstallableStatus)
