#
# PySNMP MIB module VELOCLOUD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VELOCLOUD-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:40:57 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, ObjectIdentity, Bits, Integer32, Counter64, ModuleIdentity, Counter32, Gauge32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "ObjectIdentity", "Bits", "Integer32", "Counter64", "ModuleIdentity", "Counter32", "Gauge32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
velocloud = ModuleIdentity((1, 3, 6, 1, 4, 1, 45346))
velocloud.setRevisions(('2021-05-11 00:00', '2019-08-02 00:00', '2017-01-18 00:00', '2017-01-13 00:00',))
if mibBuilder.loadTexts: velocloud.setLastUpdated('202105110000Z')
if mibBuilder.loadTexts: velocloud.setOrganization('VMware Corporation')
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 45346, 1))
mibBuilder.exportSymbols("VELOCLOUD-MIB", velocloud=velocloud, PYSNMP_MODULE_ID=velocloud, modules=modules)
