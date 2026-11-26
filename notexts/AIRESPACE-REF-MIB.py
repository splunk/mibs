#
# PySNMP MIB module AIRESPACE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/AIRESPACE-REF-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
airespace = ModuleIdentity((1, 3, 6, 1, 4, 1, 14179))
airespace.setRevisions(('2005-12-19 00:00',))
if mibBuilder.loadTexts: airespace.setLastUpdated('200512190000Z')
if mibBuilder.loadTexts: airespace.setOrganization('Airespace, Inc.')
mibBuilder.exportSymbols("AIRESPACE-REF-MIB", PYSNMP_MODULE_ID=airespace, airespace=airespace)
