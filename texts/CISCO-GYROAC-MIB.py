#
# PySNMP MIB module CISCO-GYROAC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GYROAC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, TimeTicks, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "TimeTicks", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoGyroacMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 859))
ciscoGyroacMIB.setRevisions(('2019-01-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGyroacMIB.setRevisionsDescriptions(('Latest version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGyroacMIB.setLastUpdated('201901090000Z')
if mibBuilder.loadTexts: ciscoGyroacMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGyroacMIB.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-ir800@cisco.com')
if mibBuilder.loadTexts: ciscoGyroacMIB.setDescription('This MIB module defines management objects for monitoring of\n        Gyroscope andvAccelerometer for IR8x9 routers.\n\n        Gyroscope feature provides information about Gyroscope data\n        shows G-X, Y, Z (3D gyroscope data) in mdps (milli Degrees Per\n        Second) and accelerometer feature provides information        \n        about XL-X, Y, Z (3D accelerator data) in unit\n        mg(milligram).\n\n        Accelerometer and Gyroscope functionality tracks the speed and\n        angular movement of the device.\n\n        *** ABBREVIATIONS, ACRONYMS, AND SYMBOLS ***\n\n        gyro - Gyroscope sensor of IR8x9 routers')
ciscoGyroacMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 859, 0))
ciscoGyro = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 859, 0, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoGyro.setStatus('current')
if mibBuilder.loadTexts: ciscoGyro.setDescription('An entry containing the management information for a particular\n        sensor gyroscope and accelerometer')
mibBuilder.exportSymbols("CISCO-GYROAC-MIB", ciscoGyro=ciscoGyro, PYSNMP_MODULE_ID=ciscoGyroacMIB, ciscoGyroacMIB=ciscoGyroacMIB, ciscoGyroacMIBObjects=ciscoGyroacMIBObjects)
